import pickle

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

print("📧 Email Phishing Detector (ML Model)")

# Take input
email = input("Enter email text: ")

# Transform and predict
email_vector = vectorizer.transform([email])
prediction = model.predict(email_vector)

if prediction[0] == 1:
    print("⚠️ This email is PHISHING")
else:
    print("✅ This email is SAFE")