# HematoVision 🩸
## Advanced Blood Cell Classification Using Transfer Learning

HematoVision is an AI-powered web application designed to classify microscopic blood cell images using deep learning and transfer learning techniques. The system identifies different blood cell types and presents results through an intuitive web interface.

---

## 🚀 Features
- Blood cell image classification using a pre-trained CNN
- Transfer learning for improved accuracy and reduced training time
- Flask-based web application for real-time predictions
- Displays predicted class along with confidence score
- Clean and user-friendly interface
- Ethical disclaimer for medical usage

---

## Project Demo Videos
Code Video Demo:
- https://drive.google.com/file/d/1PYBITrt_gHvEcbtuWeqUxURJwwcCpklq/view?usp=drive_link

Webpage Video Demo:
- https://drive.google.com/file/d/1vsd9BJdiq-A9_bok2KYxDwBTTgimlSA8/view?usp=drive_link

---

## 🧠 Blood Cell Classes
The model classifies blood cell images into the following categories:
- Eosinophil
- Lymphocyte
- Monocyte
- Neutrophil

---

## 🛠️ Technologies Used
- Python
- TensorFlow / Keras
- Transfer Learning (MobileNetV2)
- OpenCV
- Flask
- HTML & CSS
- Jupyter Notebook

---

## 📁 Project Structure
```
HematoVision/
│
├── app.py
├── Blood Cell.keras
├── requirements.txt
├── README.md
│
├── templates/
│   ├── home.html
│   └── result.html
│
├── static/
│   └── (empty or sample image)
│
└── notebook/
    └── model_training.ipynb
```

### Training Notebook
The complete model training pipeline, including data preprocessing, transfer learning configuration, training, and evaluation, is available in the Jupyter Notebook located at:


---

### Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/Sanjureddy-17/HematoVision.git
cd HematoVision
```

2. Create a virtual environment (optional but recommended):

``` bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask application:

```bash
python app.py
```

5. Open your browser and visit:

``` cpp
http://127.0.0.1:5000/
```

## 📊 Model Training

The deep learning model was trained using annotated blood cell images. Transfer learning was applied using a pre-trained convolutional neural network to leverage learned image features, resulting in faster convergence and improved performance.

Model training and evaluation were performed in a Jupyter Notebook, and the trained model was saved as Blood Cell.keras for deployment.

## ⚠️ Disclaimer

This application is intended for educational and research purposes only.
It should not be used as a sole basis for medical diagnosis or clinical decision-making.

