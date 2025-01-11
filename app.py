from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
import mediapipe as mp
import cv2
import json

app = Flask(__name__)

# Load the trained LSTM model
model = tf.keras.models.load_model('working/LSTM_Model_1.h5')

# Load the label map
with open("working/label_map.json", "r") as file:
    label_map = json.load(file)
    label_map = {int(v): k for k, v in label_map.items()}

# Initialize MediaPipe holistic model
mp_holistic = mp.solutions.holistic

# Global state variables
collecting = False
sequence = []
sequence_length = 48

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

@app.route('/toggle', methods=['POST'])
def toggle_collection():
    global collecting, sequence
    collecting = not collecting
    sequence = []  # Reset sequence when toggling
    status = "started" if collecting else "stopped"
    return jsonify({"status": status, "message": f"Keypoint collection {status}."})

@app.route('/collect', methods=['POST'])
def collect_keypoints():
    global collecting, sequence, sequence_length

    if not collecting:
        return jsonify({"error": "Keypoint collection is not active"}), 400

    if 'frames' not in request.files:
        return jsonify({"error": "No frames provided"}), 400

    frames = request.files.getlist('frames')  # List of frames sent in one request
    for frame in frames:
        frame = np.frombuffer(frame.read(), np.uint8)
        image = cv2.imdecode(frame, cv2.IMREAD_COLOR)

        # Process frame with MediaPipe
        with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
            results = mediapipe_detection(image, holistic)
            keypoints = extract_keypoints(results)
            sequence.append(keypoints)

    # Ensure sequence length
    if len(sequence) > sequence_length:
        sequence = sequence[-sequence_length:]

    # Make a prediction if sequence is ready
    if len(sequence) == sequence_length:
        input_sequence = np.expand_dims(np.array(sequence), axis=0)
        prediction = model.predict(input_sequence)
        predicted_label = np.argmax(prediction)
        predicted_word = label_map[predicted_label]
        confidence = float(np.max(prediction))
        return jsonify({
            "message": "Keypoints collected and prediction made.",
            "predicted_word": predicted_word,
            "confidence": confidence
        })

    return jsonify({"message": f"Keypoints collected, current sequence length: {len(sequence)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)