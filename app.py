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
    user_input = request.form["input"]
    cleaned_input = user_input.lower().strip()

    transformed_input = vectorizer.transform([cleaned_input])
    prediction = model.predict(transformed_input)[0]

    if prediction == 1:
        result = "PHISHING ⚠️"
    else:
        result = "SAFE ✅"

    return render_template("index.html", prediction_text=result)


# ✅ THIS MUST BE OUTSIDE FUNCTIONS
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)