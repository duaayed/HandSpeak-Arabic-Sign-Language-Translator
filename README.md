<h1 align="center">HandSpeak</h1>
<div align="center">
  <img src="https://github.com/user-attachments/assets/da210bca-cbf0-4a2b-83dd-32cd73147f4d" alt="logo" width="300">
  <img src="https://github.com/user-attachments/assets/066b9023-ab90-47ce-a00a-3651e1399023" alt="Poster" width="300">
</div>
<h4 align="center">Sign Language Model to Translate Arabic sign Language Into Text</h4>
<div align="center">
  <hr style="border: 3px solid black; width: 80%;">
</div>

1. [Overview](#overview)<br>
    • [Motivation](#motivation)<br>
    • [Project Aim and Objectives](#project-aim-and-objectives)<br>
    • [Project Scope](#project-scope)<br>
    • [Goals](#goals)
2. [Dataset](#dataset)
3. [Usability and User Experience Goals](#usability-and-user-experience-goals)<br>
    • [Usability Goals](#usability-goals)<br>
    • [User Experience Goals](#user-experience-goals)
4. [Preparing the Dataset](#preparing-the-dataset)<br>
    • [Data Extraction](#data-extraction)<br>
    • [Normalization](#normalization)<br>
    • [Generating Arrays](#generating-arrays)<br>
    • [Outcome](#outcome)
5. [LSTM Model](#lstm-model)<br>
    • [Model Architecture](#model-architecture)<br>
    • [Model Optimization Techniques](#model-optimization-techniques)<br>
    • [Model Parameters](#model-parameters)

<h2 align="left">Overview</h2>
Sign language consists of gestures and expressions used mainly by the hearing-impaired to talk. This project is an effort to bridge the communication gap between the hearing and the hearing-impaired community using Artificial Intelligence.
<h3 align="left">Motivation</h3>
Due to the small number of people who can read sign language, deaf people frequently experience severe communication difficulties. This leads to difficulties in accessing essential services, social exclusion, and a lack of equal opportunities. An AI-powered model that translates sign language into natural language can bridge this communication gap, fostering better interaction and inclusivity. Such a model would empower deaf people by enabling smooth communication, allowing them to access necessary resources and engage more fully in society.
<details>
  <summary><h3 align="left">Project Aim and Objectives</h3></summary>
  
  The main aim of HandSpeak is to develop an artificial intelligence model to bridge the communication gap between Arabic spoken language and Arabic sign language by translating sign language gestures into text in real-time.

  i. Understand how sign language works, and study existing solutions and algorithms related to this project. <br>
  ii. Collect and prepare a reliable dataset of sign language gestures. Then, preprocess the data to ensure it is ready for training the model. <br>
  iii. Choose and train a machine learning model to ensure accurate and consistent predictions. <br>
  iv. Evaluate the system by testing its accuracy, usability, and real-world performance to ensure it meets user needs and expectations. <br>
  v. Document the entire development process, including design, implementation, and testing, to provide a clear and organized reference for future improvements and similar projects.

</details>
<details>
  <summary><h3 align="left">Project Scope</h3></summary>
  
  The scope of this project is to develop an artificial intelligence model that translates sign language into words in real-time, enhancing communication and accessibility for the hearing-impaired community.

  i. **Ensure Real-Time Translation**: Implement real-time processing to provide immediate translation of sign language to natural language. <br>
  ii. **Support Arabic Language**: Focus on providing accurate translation for gestures specific to Arabic sign language, catering to the needs of the Arabic-speaking community. <br>
  iii. **Bridging the communication barrier**s between deaf people and the community.

</details>

<h3 align="left">Goals</h3>
1. Enable integration of sign language into existing applications. <br>
2. Improve education quality for the deaf and elevate literacy rates. <br>
3. Promote communication inclusivity of the hearing impaired. <br>


<h2 align="left">Dataset</h2>
After extensive research and evaluation of various datasets, we concluded that KArSL is the most comprehensive and reliable dataset available for Arabic Sign Language (ArSL). KArSL is the largest video dataset
specifically designed for word-level ArSL recognition, widely used across Arab countries. It contains 502 isolated sign words, each performed by three professional signers and repeated 50 times per signer.
<div align="center">
  <img src="https://github.com/user-attachments/assets/a8fec0c9-b0a4-4c68-820d-4fcc16c6a95b" alt="KARSL">
</div>
<div align="center">
  You can access the dataset here: <a href="https://hamzah-luqman.github.io/KArSL/">KARSL Dataset</a>
</div>
<br><br>

We utilized the KARSL Dataset. The dataset comprises 502 distinct sign classes, each performed by two signers. These classes were carefully curated to represent a wide range of Arabic sign language
gestures. The dataset provided a robust foundation for training and evaluating our artificial intelligence model, enabling us to bridge the communication gap between Arabic spoken language and Arabic sign language.

<br>
 <div align="center">

<table>
  <thead>
    <tr>
      <th>SignID</th>
      <th>Sign-Arabic</th>
      <th>Sign-English</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>71</td>
      <td>هيكل عظمي</td>
      <td>Skeleton</td>
    </tr>
    <tr>
      <td>72</td>
      <td>جمجمة</td>
      <td>Skull</td>
    </tr>
    <tr>
      <td>73</td>
      <td>عمود فقري</td>
      <td>Backbone</td>
    </tr>
    <tr>
      <td>74</td>
      <td>قفص صدري</td>
      <td>Chest</td>
    </tr>
    <tr>
      <td>75</td>
      <td>جهاز تنفسي</td>
      <td>Respiratory device</td>
    </tr>
    <tr>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <td>166</td>
      <td>يشم</td>
      <td>Inhale</td>
    </tr>
    <tr>
      <td>167</td>
      <td>يصعد</td>
      <td>Rise</td>
    </tr>
    <tr>
      <td>168</td>
      <td>ينزل</td>
      <td>Descend</td>
    </tr>
    <tr>
      <td>169</td>
      <td>يفتح</td>
      <td>Open</td>
    </tr>
    <tr>
      <td>170</td>
      <td>يقفل ( يغلق )</td>
      <td>Close</td>
    </tr>
  </tbody>
</table>

</div>

<br><br>
We processed the input frames from the **KARSL Dataset** to generate three specific arrays: **pose-adjusted**, **lh-adjusted**, and **rh-adjusted**. These arrays represent the adjusted keypoints for the
pose, the left hand, and the right hand, respectively. The adjustments ensured that the keypoints were normalized and aligned correctly, enabling consistent and accurate input for the model. This preprocessing step was
critical for improving the robustness and precision of our system's predictions.
<br>
<div align="center">
  <video src="https://github.com/user-attachments/assets/d3494732-097f-4553-8a7f-8e577413c3c0" controls width="600">
  </video>
</div>


<h2 align="left">Usability and User Experience Goals</h2>
The usability and user experience goals of this project were carefully designed to prioritize seamless interaction and accessibility. The primary focus was to deliver a system capable of recognizing gestures in real
time, ensuring users experience smooth and uninterrupted communication. Robust algorithms were implemented to handle diverse conditions, including variations in gestures, lighting, and camera quality, while maintaining
high accuracy. Additionally, the solution was optimized for efficiency, enabling quick response times without compromising on accuracy. By emphasizing integration with widely used communication tools, the project aimed
to make the system adaptable and valuable in various real-world scenarios, ensuring it meets the needs of a diverse user base.
<details>
  <summary><h3 align="left">Usability Goals</h3></summary>

  i. **Real-Time Performance**: Deliver seamless and real-time gesture recognition to avoid delays, ensuring smooth communication without interruptions. <br>
  ii. **Error Tolerance**: Implement robust algorithms that can adapt to variations in gestures, lighting, and camera quality, minimizing errors in recognition. <br>
  iii. **Efficiency**: Optimize the model for real-time translation, ensuring fast and accurate recognition of gestures without noticeable delays. <br>
  iv. **Integration**: Enable seamless integration with commonly used communication tools like video conferencing platforms, making the solution more versatile.

</details>

<details>
  <summary><h3 align="left">User Experience Goals</h3></summary>

  i. **Educational Value**: Incorporate features that allow non-signers to learn basic sign language gestures, fostering inclusivity and understanding. <br>
  ii. **Transparency**: Provide clear feedback to users about recognized gestures, enhancing confidence in the system’s accuracy.

</details>

<h2 align="left">Preparing the Dataset</h2>
Preparing the dataset was a critical step in building our Arabic Sign Language recognition model. We worked extensively with the KArSL Dataset, which contains a comprehensive collection of 502 isolated sign classes
performed by professional signers. This section details the key steps involved in processing the dataset to ensure it was ready for model training and evaluation.

<details>
  <summary><h3 align="left">Data Extraction</h3></summary>
  Each video was analyzed frame by frame to extract keypoints using MediaPipe. 
  <br>
  i. **Pose Keypoints**: Representing the full-body structure. <br>
  ii. **Left Hand Keypoints**: Capturing detailed movements of the left hand. <br>
  iii. **Right Hand Keypoints**: Capturing detailed movements of the right hand.

</details>

<h3 align="left">Normalization</h3>
All keypoints were normalized to remove variations caused by different scales and orientations of the input videos. This ensured that the model learned features intrinsic to the gestures rather than irrelevant variations.

<details>
  <summary><h3 align="left">Generating Arrays</h3></summary>
  Three arrays were created from the processed data<br> <br>
  
  i. **pose-adjusted**: Adjusted keypoints for the pose in each frame. <br>
  ii. **lh-adjusted**: Adjusted keypoints for the left hand in each frame. <br>
  iii. **rh-adjusted**: Adjusted keypoints for the right hand in each frame.

</details>

<h3 align="left">Challenges Faced</h3>
• Variations in Gestures: Similar starting or ending gestures across different classes required careful preprocessing to ensure clear differentiation.

• Lighting and Background Differences: Frames were preprocessed to mitigate the impact of varying environmental conditions on keypoint detection.


<h3 align="left">Outcome</h3>
The prepared dataset was optimized for input into the Bidirectional LSTM model. By focusing on normalized and adjusted keypoints, we ensured that the model could learn robustly from the sequential data, leading to high
accuracy in gesture recognition. This step played a pivotal role in the success of the project.


<h2 align="left">LSTM Model</h2>

<h3 align="left">Model architecture</h3>
To develop our Arabic sign language model, we utilized a BiLSTM architecture, which is an extension of the Long Short-Term Memory (LSTM) network. LSTM, a type of Recurrent Neural Network (RNN), is specifically designed
to model and analyze sequential data. It excels in handling long sequences by selectively retaining or discarding information at each time step, enabling it to capture long-range dependencies and make accurate
predictions.

In our study, we observed that many signs in the dataset shared similar starting or ending gestures. This overlap in sequential patterns made the bidirectional nature of BiLSTM particularly valuable. By processing the
data in both forward and backward directions, BiLSTM allowed the model to better capture contextual dependencies from both ends of the sequence, leading to more precise and reliable gesture recognition. This made BiLSTM
the ideal choice for addressing the challenges posed by the intricate structure of our dataset.


<h3 align="left">Python</h3>

```python
# Define the Bidirectional LSTM model with Attention

model = tf.keras.Sequential([
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, return_sequences=True)),
    tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(len(words), activation='softmax')
])

# Compile the model

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])

# Set up early stopping
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',  # Metric to monitor for early stopping
    mode='min',  # Set mode to 'min' for minimizing the metric
    patience=5,  # Number of epochs with no improvement before stopping
    restore_best_weights=True,  # Restore the best model weights
    verbose=1
)

model_training_history = model.fit(
    X_train, y_train, 
    batch_size=32, 
    validation_data=(X_val, y_val), 
    validation_batch_size=32, 
    epochs=50, 
    callbacks=[early_stopping]
)
```
<br>
<div align="center">
  <img src="https://github.com/user-attachments/assets/542b4fe0-3810-4da5-b920-5392b3c9b526" alt="Model">
  <img src="https://github.com/user-attachments/assets/ebc61cf6-db05-462d-8fa8-2ef778d9d28e" alt="Model_2" width="500">
</div>

<h3 align="left">Model Optimization techniques</h3>
• Early Stopping Technique <br>
The early stopping technique is used to reduce overfitting without compromising on the
model’s accuracy. It consists of stopping training the model when the validation loss begins to
increase while the training loss continues to decrease.

<div align="center">
  <img src="https://github.com/user-attachments/assets/66fd95b2-c29d-4513-84f0-64e35e939d3f" alt="Early_Stopping">
</div>

• Adam Optimization Algorithm <br>
Adam is an optimization algorithm that can be used instead of the classical stochastic gradient descent procedure to update network weights iterative based in training data.[14]
It offers adaptive learning rates, which dynamically adjust the learning rate for each parameter based on past gradients. This adaptivity provides faster convergence and improves performance across various data and model
architectures.

<h3 align="left">Model Parameters</h3>

<table>
  <thead>
    <tr>
      <th>Argument</th>
      <th>Type</th>
      <th>Default</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>layers</b></td>
      <td>list</td>
      <td>2 Bidirectional LSTM, 2 Dense</td>
      <td>Defines the model architecture: 2 Bidirectional LSTM layers followed by Dense layers for classification.</td>
    </tr>
    <tr>
      <td><b>units</b></td>
      <td>int</td>
      <td>64</td>
      <td>Number of units (hidden neurons) in each LSTM layer.</td>
    </tr>
    <tr>
      <td><b>activation_dense</b></td>
      <td>str</td>
      <td>relu and softmax</td>
      <td>Activation functions for Dense layers: relu for the hidden layer and softmax for the output layer.</td>
    </tr>
    <tr>
      <td><b>optimizer</b></td>
      <td>str</td>
      <td>adam</td>
      <td>Optimization algorithm for training.</td>
    </tr>
    <tr>
      <td><b>loss</b></td>
      <td>str</td>
      <td>categorical_crossentropy</td>
      <td>Loss function for multi-class classification tasks.</td>
    </tr>
    <tr>
      <td><b>metrics</b></td>
      <td>list</td>
      <td>['categorical_accuracy']</td>
      <td>Metrics to evaluate the model's performance during training.</td>
    </tr>
    <tr>
      <td><b>batch_size</b></td>
      <td>int</td>
      <td>32</td>
      <td>Number of samples per batch for training and validation.</td>
    </tr>
    <tr>
      <td><b>epochs</b></td>
      <td>int</td>
      <td>50</td>
      <td>Maximum number of training iterations.</td>
    </tr>
    <tr>
      <td><b>early_stopping</b></td>
      <td>dict</td>
      <td>See description</td>
      <td>Early stopping configuration to prevent overfitting. Monitors <code>val_loss</code>, with patience of 5 epochs.</td>
    </tr>
    <tr>
      <td><b>validation_split</b></td>
      <td>float</td>
      <td>0.2</td>
      <td>Fraction of training data used for validation (20%).</td>
    </tr>
    <tr>
      <td><b>input_shape</b></td>
      <td>tuple</td>
      <td>(frames, features)</td>
      <td>Input shape for the LSTM model, determined by the preprocessed sequence length and features.</td>
    </tr>
    <tr>
      <td><b>output_classes</b></td>
      <td>int</td>
      <td>len(words)</td>
      <td>Number of classes in the output layer, based on the unique words/signs in the dataset.</td>
    </tr>
  </tbody>
</table>
