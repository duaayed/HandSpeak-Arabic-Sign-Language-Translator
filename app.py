from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import mediapipe as mp
import cv2
import json

app = Flask(__name__)

# Load the trained LSTM model
model = tf.keras.models.load_model('working/LSTM_Model_1.h5')  # Replace with the correct path to your model

# Load the label map
with open("working/label_map.json", "r") as file:  # Replace with the correct path
    label_map = json.load(file)
    label_map = {int(v): k for k, v in label_map.items()}  # Reverse key-value for decoding predictions

# Initialize MediaPipe holistic model
mp_holistic = mp.solutions.holistic

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = model.process(image)
    image.flags.writeable = True
    return results

def extract_keypoints(results):
    pose = np.array([[res.x, res.y, res.z] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*3)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3)
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3)
    return np.concatenate([pose, lh, rh])

@app.route('/predict', methods=['POST'])
def predict():
    if 'frames' not in request.files:
        return jsonify({"error": "No frames provided"}), 400
    
    frames = request.files.getlist('frames')  # Multiple frames sent
    keypoints_sequence = []
    
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        for frame in frames:
            frame = np.frombuffer(frame.read(), np.uint8)
            image = cv2.imdecode(frame, cv2.IMREAD_COLOR)
            results = mediapipe_detection(image, holistic)
            keypoints = extract_keypoints(results)
            keypoints_sequence.append(keypoints)
    
    # Pad or truncate to the fixed input length (e.g., 48 frames)
    f_avg = 48
    if len(keypoints_sequence) < f_avg:
        while len(keypoints_sequence) < f_avg:
            keypoints_sequence.append(keypoints_sequence[-1])  # Pad with the last frame
    else:
        keypoints_sequence = keypoints_sequence[:f_avg]
    
    # Convert to numpy array and reshape for model input
    keypoints_sequence = np.expand_dims(np.array(keypoints_sequence), axis=0)  # Shape: (1, 48, n_features)
    
    # Make a prediction
    prediction = model.predict(keypoints_sequence)
    predicted_label = np.argmax(prediction)
    predicted_word = label_map[predicted_label]
    
    return jsonify({"predicted_word": predicted_word})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
