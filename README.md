# 🔐 Email Spam & Phishing Detector

A machine learning-based web application that detects whether an email is **Safe** or **Phishing**.

---

## 🚀 Features

* Analyze full email content (not just short text)
* Detect phishing using a trained ML model
* Clean and professional web interface
* Real-time prediction using Flask

---

## 🧠 Tech Stack

* Python
* Flask
* Scikit-learn
* HTML & CSS

---

## 📂 Project Structure

phishing-email-detector/
│
├── app.py                # Flask backend
├── templates/
│   └── index.html       # Frontend UI
├── model.pkl            # Trained ML model
├── vectorizer.pkl       # TF-IDF vectorizer
├── train_model.py       # Model training script
├── save_model.py        # Model saving script
├── .gitignore
└── README.md

---

## ▶️ How to Run the Project

```bash
# Step 1: Download the project from GitHub
git clone <your-repo-link>

# Step 2: Move into the project folder
cd phishing-email-detector

# Step 3: Create a virtual environment (keeps dependencies organized)
python3 -m venv venv

# Step 4: Activate the virtual environment
source venv/bin/activate

# Step 5: Install required libraries
pip install flask scikit-learn

# Step 6: Start the application
python app.py
```

Open your browser and go to:
http://127.0.0.1:5000/

---

## 🎯 Example

Paste a full email like:

Subject: Urgent Account Verification

Dear user,
Your account has been compromised.
Click the link below immediately:
http://fake-link.com

➡️ The model will classify it as **PHISHING ⚠️** or **SAFE ✅**

---

## 👩‍💻 Author

Anushka Patidar

---

⚡ Built as a cybersecurity and machine learning project
