<h1 align="center">HandSpeak</h1>
<div align="center">
  <img src="https://github.com/user-attachments/assets/da210bca-cbf0-4a2b-83dd-32cd73147f4d" alt="logo" width="200">
  <img src="https://github.com/user-attachments/assets/04911c8b-8202-4d12-82ac-5832100537ce" alt="Untitled design" width="200">
</div>
<h4 align="center">Sign Language Model to Translate Arabic sign Language Into Text</h4>
<div align="center">
  <hr style="border: 3px solid black; width: 80%;">
</div>
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

  i. Ensure Real-Time Translation: Implement real-time processing to provide immediate translation of sign language to natural language. <br>
  ii. Support Arabic Language: Focus on providing accurate translation for gestures specific to Arabic sign language, catering to the needs of the Arabic-speaking community. <br>
  iii. Bridging the communication barriers between deaf people and the community.

</details>

<h3 align="left">Goals</h3>
1. Enable integration of sign language into existing applications. <br>
2. Improve education quality for the deaf and elevate literacy rates. <br>
3. Promote communication inclusivity of the hearing impaired. <br>


<h2 align="left">Dataset</h2>
After extensive research and evaluation of various datasets, we concluded that KArSL is the most comprehensive and reliable dataset available for Arabic Sign Language (ArSL). KArSL is the largest video dataset specifically designed for word-level ArSL recognition, widely used across Arab countries. It contains 502 isolated sign words, each performed by three professional signers and repeated 50 times per signer.
<div align="center">
  <img src="https://github.com/user-attachments/assets/a8fec0c9-b0a4-4c68-820d-4fcc16c6a95b" alt="logo">
</div>
<div align="center">
  You can access the dataset here: <a href="https://hamzah-luqman.github.io/KArSL/">KARSL Dataset</a>
</div>

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
      <td>166</td>
      <td>شم</td>
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
      <td>يغلق ( يغلق )</td>
      <td>Close</td>
    </tr>
  </tbody>
</table>

</div>
