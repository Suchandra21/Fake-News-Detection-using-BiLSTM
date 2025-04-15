📰 Fake News Detection with BiLSTM
A deep learning-powered web application to detect fake news in real-time using a Bidirectional LSTM model.

🚀 Project Overview
This project implements a fake news classification model using Bidirectional LSTM (BiLSTM). It includes:

- A deep learning model trained on real/fake news headlines.

- A Flask-based web app for real-time prediction.

- Deployed on AWS EC2 for public access.

📂 Repository Structure
```bash
├── app.py                         # Flask backend
├── index.html                    # Frontend template
├── fake_news_model.h5            # Trained Keras model
├── tokenizer.json                # Tokenizer used during training
├── requirement.txt               # Python dependencies
├── Note_book_of_Fake_news_detection_using_DL.ipynb  # Jupyter notebook with full pipeline
```

🧠 Model Architecture
Embedding Layer

- Bidirectional LSTM (100 units)
- LSTM (50 units)
- Dropout (0.3)
- Dense (Softmax) for binary classification

Training enhancements:

- Text preprocessing using nltk + sklearn
- Data augmentation via nlpaug
- Handling class imbalance with computed weights

📊 Results

Metric	Score
Accuracy	~96% on test data
AUC Score	~0.98
F1 Score	~0.96
Visual outputs include:

- 📈 Loss/Accuracy Curves
- 📊 Confusion Matrix
- 📉 ROC Curve

🌐 Live Demo
🖥️ Deployed on: AWS EC2 Instance

-- You can run it locally by following the instructions below.

🛠️ Installation
```bash
# Clone the repository
git clone https://github.com/your-username/Fake-News-Detection.git
cd Fake-News-Detection

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirement.txt
```

🧪 Usage
```bash
# Run the Flask server
python app.py
```
- Open your browser and go to: http://127.0.0.1:5000
- Enter any news text and get real-time predictions: ✅ Real / ❌ Fake

📸 Screenshots
![Screenshot 2025-02-17 104441](https://github.com/user-attachments/assets/ea36f1a0-c5d1-42a7-a7b2-3aeb10730ca6)

🙌 Acknowledgements
- Kaggle Dataset.
- Libraries: TensorFlow, Flask, NLPAug, NLTK, sklearn

