import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Sample dataset (we'll use real later)
data = {
    "email": [
        "Win money now",
        "Urgent! Click here",
        "Meeting at 5 pm",
        "Let's have lunch",
        "Claim your prize now",
        "Project deadline tomorrow"
    ],
    "label": [1, 1, 0, 0, 1, 0]  # 1 = phishing, 0 = safe
}

df = pd.DataFrame(data)

# Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["email"])

y = df["label"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Test prediction
test_email = ["Urgent! You won a prize"]
test_vector = vectorizer.transform(test_email)

prediction = model.predict(test_vector)

if prediction[0] == 1:
    print("⚠️ Phishing Email Detected")
else:
    print("✅ Safe Email")