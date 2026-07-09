# 🌸 Basic Image Recognition System using TensorFlow

## 📖 Overview

The Basic Image Recognition System is a deep learning project developed using Python and TensorFlow. The system is trained to recognize different types of flowers from images using a Convolutional Neural Network (CNN). It predicts the flower category along with the confidence score.

This project was developed as part of an AI Internship task.

---

## 🎯 Objectives

- Build a basic image recognition model.
- Train a CNN using a flower image dataset.
- Predict the class of a new flower image.
- Display the prediction with confidence.

---

## 🌼 Flower Categories

The model recognizes the following five flower classes:

- Daisy
- Dandelion
- Roses
- Sunflowers
- Tulips

---

## 🛠 Technologies Used

- Python 3
- TensorFlow
- Keras
- NumPy
- Pillow

---

## 📂 Project Structure

```
Basic-Image-Recognition-System/
│
├── train.py
├── prediction.py
├── flower_model.keras
├── test.jpg
├── requirements.txt
├── README.md
└── Dataset/
    ├── daisy/
    ├── dandelion/
    ├── roses/
    ├── sunflowers/
    └── tulips/
```

---

## ⚙ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Basic-Image-Recognition-System.git
```

Move to the project folder:

```bash
cd Basic-Image-Recognition-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 Training the Model

Run the following command:

```bash
python train.py
```

After training, the model will be saved as:

```
flower_model.keras
```

---

## 🖼 Testing the Model

Place a flower image in the project folder and rename it:

```
test.jpg
```

Run:

```bash
python prediction.py
```

---

## 📌 Sample Output

```
========================================
Flower Recognition Result
========================================
Predicted Flower : Sunflower
Confidence        : 98.45%
========================================
```

---

## ✨ Features

- Image Recognition using CNN
- Five Flower Classification
- Confidence Score Prediction
- Easy to Train
- Easy to Test
- Beginner-Friendly AI Project

---

## 📦 Requirements

- Python 3.10 or above
- TensorFlow
- NumPy
- Pillow

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- Add more flower categories
- Develop a graphical user interface (GUI)
- Create a web application using Flask
- Real-time image recognition using a webcam

---

## 👩‍💻 Author

**Ayesha Yaqoob**

BS Computer Science

University of Narowal

AI Internship Project
