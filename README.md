<img width="1920" height="1140" alt="Screenshot 2026-06-04 110125" src="https://github.com/user-attachments/assets/52158e5c-39f4-43b0-8b2e-beb56e9236a0" />


# ✍️ Handwritten Digit Recognition using CNN

A deep learning web application that recognizes handwritten digits (0–9) using a Convolutional Neural Network (CNN) trained on the MNIST dataset. Users can draw digits directly on an interactive canvas, and the model predicts the digit in real time.


---

## 📌 Project Overview

Handwritten digit recognition is one of the fundamental applications of Computer Vision and Deep Learning.

This project uses a Convolutional Neural Network (CNN) trained on the MNIST dataset to classify handwritten digits from 0 to 9. The application provides an interactive drawing canvas where users can draw a digit and instantly receive a prediction with confidence scores.

---

## 🎯 Features

- Interactive drawing canvas
- Real-time digit prediction
- CNN-based image classification
- Confidence score display
- User-friendly Streamlit interface
- Trained on the MNIST dataset
- High prediction accuracy (~99%)

---

## 🧠 Technologies Used

- Python
- TensorFlow / Keras
- CNN (Convolutional Neural Network)
- NumPy
- Pillow (PIL)
- Streamlit
- Streamlit Drawable Canvas

---

## 📂 Project Structure

```text
handwritten_digit_recognition/
│
├── models/
│   └── digit_cnn_model.keras
│
├── screenshots/
│   ├── home_page.png
│   ├── prediction_result_0.png
│   ├── prediction_result_2.png
│   ├── prediction_result_5.png
│   └── prediction_result_7.png
│
├── train.py
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Dataset

### MNIST Dataset

The model is trained using the MNIST handwritten digit dataset.

- Total Images: 70,000
- Training Images: 60,000
- Testing Images: 10,000
- Image Size: 28 × 28 pixels
- Classes: 10 (Digits 0–9)

---

## 🏗️ Model Architecture

```text
Input Layer (28×28×1)

↓ Conv2D (32 Filters)

↓ MaxPooling2D

↓ Conv2D (64 Filters)

↓ MaxPooling2D

↓ Flatten

↓ Dense (128 Neurons)

↓ Output Layer (10 Classes)
```

---

## 📈 Model Performance

| Metric | Value |
|----------|----------|
| Test Accuracy | 98.96% |
| Dataset | MNIST |
| Model Type | CNN |
| Classes | 10 |

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/hasiniambati23/CodeAlpha_Handwritten_Digit_Recognition.git
cd CodeAlpha_Handwritten_Digit_Recognition
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

#### Windows

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🏋️ Train the Model

```bash
python train.py
```

The trained model will be saved inside:

```text
models/digit_cnn_model.keras
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Home Page
<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/eed67117-dd9b-4c1f-a4b8-3a969d6c074a" />

### Prediction_result_0.png
<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/56a2b1b7-abc9-4cb1-ae96-51421fd52ded" />

### Prediction_result_2.png
<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/1819287e-fe04-4f09-ab53-570b9c8912dc" />

### Prediction_result_5.png
<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/e20ef3ff-768b-4261-93af-76460bbc96a5" />

### Prediction_result_7.png
<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/455b45e4-d540-440b-ae50-6d56454dab5b" />

---

## 🚀 Live Demo
[Open Application]()

## 🔮 Future Improvements

- Support custom uploaded images
- Improved preprocessing techniques
- Digit probability visualization
- Mobile-friendly interface
- Advanced CNN architectures

---

## 👩‍💻 Author

Hasini Reddy

Machine Learning Internship Project
