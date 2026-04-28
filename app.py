from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# 🔹 Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # 🔹 Get full email input
    user_input = request.form["input"]

    # 🔹 Clean text (important for full emails)
    cleaned_input = user_input.lower().strip()

    # 🔹 Convert text → numerical features
    transformed_input = vectorizer.transform([cleaned_input])

    # 🔹 Predict
    prediction = model.predict(transformed_input)[0]

    # 🔹 Convert result to readable output
    if prediction == 1:
        result = "PHISHING ⚠️"
    else:
        result = "SAFE ✅"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)