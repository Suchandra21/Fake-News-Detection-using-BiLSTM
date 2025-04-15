from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
import numpy as np
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# Download stopwords
nltk.download('stopwords')

app = Flask(__name__)

# Load Trained Model
model = tf.keras.models.load_model("fake_news_model.h5")

# Load Tokenizer
with open("tokenizer.json", "r") as f:
    tokenizer_json = json.load(f)
tokenizer = tokenizer_from_json(json.dumps(tokenizer_json))  # Fix TypeError issue

# Define Preprocessing Function
custom_stopwords = set(stopwords.words('english')).union(ENGLISH_STOP_WORDS)

def preprocess_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)  # Remove non-alphabetic characters
    text = text.lower()  # Convert to lowercase
    words = text.split()
    words = [word for word in words if word not in custom_stopwords]  # Remove stopwords
    return ' '.join(words)

# Serve HTML file at root
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# Prediction Endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json  # Expecting JSON with {"text": "your news article"}
        text = data.get("text", "")

        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Preprocess Text
        cleaned_text = preprocess_text(text)
        sequence = tokenizer.texts_to_sequences([cleaned_text])
        max_length = 256  # Same as used in training
        padded_seq = pad_sequences(sequence, maxlen=max_length, padding="post")

        # Make Prediction
        prediction = model.predict(padded_seq)
        predicted_label = np.argmax(prediction, axis=1)[0]

        # Map Prediction to Label
        label_mapping = {0: "Fake ❌", 1: "Real ✅"}
        result = label_mapping.get(predicted_label, "Unknown")

        return jsonify({"prediction": result})

    except Exception as e:
        return jsonify({"error": f"Something went wrong: {str(e)}"}), 500

# Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
