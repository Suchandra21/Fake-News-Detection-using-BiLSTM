# 📰 Fake News Detection using Deep Learning (BiLSTM)

A deep learning-based system to classify news articles as **Real** or **Fake** using a **Bidirectional LSTM** model. The project features a real-time prediction web app built with **Flask** and deployed on **AWS EC2**.
---

## 🚀 Demo

👉 **[Click here to watch the video demo](https://drive.google.com/file/d/1gy4a_SLTJKc7IYXLDvHw9BRuImU6MMqx/view?usp=sharing)**

---
## 🧠 Overview

This project uses:
- Natural Language Processing (NLP) for text preprocessing
- Data augmentation with `nlpaug`
- A **BiLSTM** neural network for classification
- Flask web app for real-time prediction
- Deployed on AWS EC2

---
## 📁 Repository Structure

```
📦 Fake-News-Detection/
├── app.py                        # Flask backend
├── fake_news_model.h5           # Trained BiLSTM model
├── tokenizer.json               # Tokenizer for inference
├── requirement.txt              # Required dependencies
├── templates/
│   └── index.html               # Frontend HTML for prediction
├── Note_book_of_Fake_news_detection_using_DL.ipynb  # Model building notebook
```

---
## 📊 Dataset

The dataset used for this project combines real and fake news articles.

- Dataset name: `fake-news dataset.zip`
- Source: [click here to download the dataset](https://drive.google.com/file/d/1MI_94iVTyMZFvqCDxZ9ShviTPN8W_0Z9/view?usp=drive_link)
- Classes:
  - `0` → Fake News
  - `1` → Real News

---

## 📊 Results

- ✅ Accuracy: **~95%**
- 📉 Confusion Matrix
- 📋 Classification Report
- 📊 ROC-AUC Curve
---

# 📜 Report
- A detailed project report includes:
- Data preprocessing techniques
- Model architectur
- Performance metrics
- Flask app architecture
- Deployment steps on AWS EC2

**👉 [View Full Report](https://docs.google.com/document/d/1Vr7RASx3K_mh8GUrx7cDIUQjSMiMuBiH/edit?usp=sharing&ouid=114715620096742571852&rtpof=true&sd=true)**

---


## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Suchandra21/Fake-News-Detection-using-BiLSTM
cd Fake-News-Detection-using-BiLSTM
```

### 2️⃣ Install dependencies
```bash
pip install -r requirement.txt
```

### 3️⃣ Run the Flask web app
```bash
python app.py
```

- Open your browser and go to: `http://127.0.0.1:5000`
- Enter any news text and get real-time predictions: ✅ Real / ❌ Fake
---

## ☁️ Deployment

Deployed on an AWS EC2 instance:
- OS: Ubuntu
- Python 3.x
- Flask for backend

---

📸 Screenshots
![Screenshot 2025-02-17 104441](https://github.com/user-attachments/assets/ea36f1a0-c5d1-42a7-a7b2-3aeb10730ca6)
---



🙌 Acknowledgements
- Kaggle Dataset.
- Libraries: TensorFlow, Flask, NLPAug, NLTK, sklearn

**If you found this project helpful, please consider giving it a ⭐ star!**

