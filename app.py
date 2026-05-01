# app.py — REPLACE YOUR ENTIRE FILE WITH THIS

from flask import Flask, render_template, request
import pickle
import re

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', ' url ', text)
    text = re.sub(r'\d+', ' num ', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    user_input = request.form["input"]
    cleaned = clean_text(user_input)
    transformed = vectorizer.transform([cleaned])
    prediction = model.predict(transformed)[0]
    confidence = model.predict_proba(transformed)[0]
    confidence_pct = round(max(confidence) * 100, 1)

    if prediction == 1:
        result = f"⚠️ PHISHING DETECTED ({confidence_pct}% confidence)"
    else:
        result = f"✅ SAFE EMAIL ({confidence_pct}% confidence)"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)