import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Training data
data = {
    "email": [
        "Win money now",
        "Urgent! Click here",
        "Meeting at 5 pm",
        "Let's have lunch",
        "Claim your prize now",
        "Project deadline tomorrow"
    ],
    "label": [1, 1, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["email"])
y = df["label"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model saved successfully!")