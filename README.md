**Forgery Detection Platform**


You're one step closer to a spam-free world

---

**Overview:**

The Forgery Detection Platform is a comprehensive solution designed to detect and classify fraudulent content across both text and image modalities. Leveraging cutting-edge techniques in Computer Vision (CV), Natural Language Processing (NLP), and Deep Learning (DL), the platform offers robust forgery detection capabilities, empowering users to identify and mitigate the risks associated with manipulated or falsified content.

---

**Key Features:**

1. **Multimodal Forgery Detection:** Utilizes CV, NLP, and DL techniques to analyze and classify both text and image content for signs of forgery or manipulation.

2. **Computer Vision (CV):**
   - _Image Forgery Detection_: CV techniques, including Convolutional Neural Networks (CNNs) such as VGG16, VGG19, and Error Level Analysis (ELA), are employed to analyze and classify images for signs of manipulation or forgery.
   - _Feature Extraction_: Pretrained CNN models are utilized to extract high-level features from images, enabling the identification of subtle alterations or inconsistencies indicative of image tampering.
   - _Forensic Analysis_: Techniques like ELA enable the identification of regions within images that exhibit irregularities in compression levels, aiding in the detection of forged or manipulated content.


3. **Natural Language Processing:**
   - _Text Forgery Detection_: NLP methods are applied to analyze and classify textual content for signs of forgery or manipulation.
   - _Preprocessing_: Text preprocessing techniques, such as tokenization, stop word removal, and stemming, are employed to clean and normalize textual data, reducing noise and enhancing the quality of analysis.
   - _Modeling_: LSTM (Long Short-Term Memory) networks are trained on preprocessed text data to learn patterns and linguistic cues indicative of fraudulent content.

4. **Deep Learning (DL):**
   - _Multimodal Fusion_: DL techniques facilitate the integration of information from both text and image modalities, enabling the platform to perform multimodal forgery detection.
   - _Model Training and Fine-Tuning_: Deep learning models, including pretrained CNNs and LSTM networks, are trained and fine-tuned on large datasets of labeled examples, enabling them to learn complex patterns and features associated with both text and image forgery.
   - _Classification_: DL models are utilized to classify content as authentic or forged based on learned representations, enabling the platform to provide accurate and reliable forgery detection results.

5. **Project Deployment:**
   - The project is deployed using Python's GUI PYQT5 library

---
**Project Workflow**
![Purple and Green Minimalist Color Blocks Concept Map Chart](https://github.com/AnushkaMazumdar2/3rd-Semester-Final-Project/assets/140642505/1e5144b6-9ef1-4025-bf4a-5d55727cc75a)


---
**Methodology**
The project consists of two parts: Image and Text Forgery Detection

1. **Image Forgery Detection**:
   - Model Testing: This module consists of the testing of our pre-trained models. The models: "Error Level Analysis", "VGG-16" and "VGG-19" were trained on the forensic benchmark dataset: CASIA v2. One can test using these pre-trained models against tampered and authentic images to check which is authentic and which is not.
   - Model Training: This module will allow users to train these models on their own customised datasets. 
   - Model Testing on Re-trained Models: This module allows users to test on the newly trained models that has been stored locally in their systems.

3. **Text Forgery Detection**:
   - Model Testing: This module allows users to test on models such as "DistilBERT" and "LSTM", which have been trained on the dataset: Spam Classification Model. 

---
**Effectiveness and Benefits:**

- _Comprehensive Forgery Detection_: The integration of CV, NLP, and DL techniques enables the platform to perform comprehensive forgery detection across both text and image modalities, offering users a holistic solution for identifying fraudulent content.
- _Enhanced Accuracy and Robustness_: By leveraging multiple modalities and deep learning models, the platform achieves enhanced accuracy and robustness in forgery detection, effectively identifying sophisticated manipulation techniques employed by malicious actors.
- _Interpretability and Visualization_: The platform provides intuitive visualization tools to aid users in interpreting forgery detection results, including ELA-highlighted regions in images and classification outcomes for textual content, enhancing transparency and usability.
- _Scalability and Adaptability_: CV, NLP, and DL techniques offer scalability and adaptability, allowing the platform to handle diverse types of forgery across various domains and applications, from social media content moderation to document authentication.

---

---
**Demonstration Video:**
Watch our demonstration video to see our Text and Image Forgery Detection Platform in action! In this video, we showcase how our platform effectively detects fraudulent text and image content using advanced Natural Language Processing (NLP), Computer Vision (CV), and Deep Learning (DL) techniques.



---

**Usage:**

1. **Installation:**
   - Clone the repository to your local machine.
   - Install the required dependencies using `pip install -r requirements.txt`.

2. **Running the Platform:**
   - Execute the main script (`Main_window_Final.py`) to launch the Forgery Detection Platform GUI.
   - Browse or input text/image content for forgery detection.
   - Click the "Test" button to initiate forgery detection and view results.

3. **Contributing:**
   - Contributions to the Forgery Detection Platform are welcome! Feel free to submit bug reports, feature requests, or pull requests via GitHub.

---

**Acknowledgments:**

- The Forgery Detection Platform utilizes pretrained models and techniques from the following sources:
  - Hugging Face Transformers Library: https://huggingface.co/transformers/
  - TensorFlow Hub: https://tfhub.dev/
  - Keras Applications: https://keras.io/api/applications/
  - OpenCV: https://opencv.org/
  - NLTK: https://www.nltk.org/

---



**References:**

- For more information on forgery detection techniques and methodologies, refer to the following resources:
  - "Digital Image Forensics" by Husrev Taha Sencar and Nasir Memon
  - "Natural Language Processing with Python" by Steven Bird, Ewan Klein, and Edward Loper
  - "Deep Learning" by Ian Goodfellow, Yoshua Bengio, and Aaron Courville


