# train_model.py — REPLACE YOUR ENTIRE FILE WITH THIS

import pandas as pd
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# ✅ Much larger and realistic dataset
data = {
    "email": [
        # PHISHING (label = 1)
        "Dear user, your account has been compromised. Click here immediately to verify: http://fake-bank.com/login",
        "Congratulations! You have won $1,000,000. Claim your prize now by clicking this link.",
        "URGENT: Your PayPal account is suspended. Verify your identity now or lose access permanently.",
        "Your bank account needs immediate verification. Login here: http://scam-site.net",
        "You have a pending payment. Click the link to confirm your details and receive your funds.",
        "Dear customer, unusual activity detected on your account. Reset password immediately.",
        "FREE iPhone 15 giveaway! You are selected. Click here to claim before it expires.",
        "IRS Tax Refund: You are eligible for a $3,200 refund. Submit your details to claim.",
        "Alert: Your credit card has been charged $499. If not you, click here to cancel.",
        "Your Netflix subscription has expired. Update payment info to continue watching.",
        "Amazon: Your order has been cancelled. Click to reactivate and get a 50% refund.",
        "FINAL WARNING: Your Microsoft account will be deleted. Verify immediately.",
        "You have been selected for a $500 Walmart gift card. Claim now, limited time!",
        "Security Alert: Someone signed into your account from a new device. Confirm or block.",
        "Dear winner, you have been selected in our lottery. Send us your bank details.",
        "Your package could not be delivered. Click to reschedule and enter your address.",
        "Urgent: Your email storage is full. Click here to upgrade or lose your emails.",
        "We detected a login from Russia. If this was not you, secure your account now.",
        "Your Apple ID has been locked. Verify your identity to unlock: http://apple-verify.ru",
        "Act now! Your Social Security Number has been suspended due to suspicious activity.",
        # SAFE (label = 0)
        "Hi team, please find attached the agenda for tomorrow's 10am project meeting.",
        "Hey, are you free for lunch on Friday? Let me know and we can plan something.",
        "The quarterly report is ready. Please review the document before the board meeting.",
        "Reminder: Your dentist appointment is scheduled for Monday at 2:30 PM.",
        "Thanks for your purchase! Your order #12345 will arrive by Thursday.",
        "Please complete the attached performance review form by end of this week.",
        "Good morning! Just checking in on the status of the design mockups.",
        "The meeting has been rescheduled to 3pm. Conference room B. See you there.",
        "Happy birthday! Hope you have a wonderful day filled with joy.",
        "Your flight booking confirmation: Flight AI202, Departure 9:00 AM, Gate 14.",
        "Hi Anushka, welcome to the internship program! Your start date is June 1st.",
        "The library book you reserved is now available for pickup.",
        "Monthly newsletter: Here are the top 5 Python tips for this month.",
        "Your subscription renewal is in 7 days. No action needed unless you want to cancel.",
        "Team lunch is happening this Thursday at 1pm at the office cafeteria.",
        "Please review and sign the updated terms of service at your convenience.",
        "Congratulations on completing the course! Your certificate is attached.",
        "Reminder to submit your timesheet by 5pm today. Thank you.",
        "Hi, I wanted to follow up on our conversation from last week about the project.",
        "The new software update is available. It includes performance improvements and bug fixes.",
    ],
    "label": [1]*20 + [0]*20
}

df = pd.DataFrame(data)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+', ' url ', text)   # replace URLs with token
    text = re.sub(r'\d+', ' num ', text)        # replace numbers
    text = re.sub(r'[^a-z\s]', ' ', text)       # remove special chars
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df["email"] = df["email"].apply(clean_text)

X_train, X_test, y_train, y_test = train_test_split(df["email"], df["label"], test_size=0.2, random_state=42)

# ✅ TF-IDF is much better than CountVectorizer for email detection
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# ✅ Logistic Regression is more accurate than Naive Bayes for this
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

print("Model Accuracy Report:")
print(classification_report(y_test, model.predict(X_test_vec)))

# Save both files
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ model.pkl and vectorizer.pkl saved successfully!")