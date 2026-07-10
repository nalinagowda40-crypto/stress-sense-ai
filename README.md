# Stress Sencs AI – Predictive Student Stress Detection & Smart Campus Support System

## 🚀 Overview
Stress Sencs AI is an innovative end-to-end college project designed to predict and detect student stress levels before exams using multimodal AI inputs. It combines facial emotion recognition, voice stress analysis, typing behavior, and wellbeing surveys into a comprehensive stress score, providing personalized interventions and admin insights.

---

## 🏗️ Project Architecture
The system follows a modern full-stack architecture:
- **Frontend**: Mobile-friendly Web App (Bootstrap 5, Chart.js, HTML/CSS/JS)
- **Backend**: Flask (Python) with RESTful APIs
- **Database**: MySQL (Student records, logs, stress scores, alerts)
- **AI Modules**:
  - **Facial Emotion Recognition**: CNN model trained on FER2013 using TensorFlow/Keras and OpenCV.
  - **Voice Stress Analysis**: Librosa library for extracting pitch, tone, and speech rate.
  - **Behaviour Analysis**: Typing speed, hesitation, and error rate tracking.
  - **Survey Analysis**: Multi-point wellbeing questionnaire.

---

## 📂 Folder Structure
```
StressSencsAI/
├── app/
│   ├── static/          # CSS, JS, Images
│   ├── templates/       # HTML templates (Student & Admin)
│   ├── models/          # SQLAlchemy Models (MySQL Schema)
│   ├── routes/          # REST API & Page Routes
│   ├── services/        # AI & Business Logic (Emotion, Voice, Scoring, Alerts)
│   ├── __init__.py      # App Factory
│   └── config.py        # App Configuration
├── data/                # Pre-trained CNN Models (.h5 files)
├── app.py               # Entry Point
├── requirements.txt     # Python Dependencies
├── schema.sql           # Database Schema (SQL)
└── README.md            # Documentation
```

---

## 📊 Stress Score Formula
The system calculates a total stress score using the following weighted formula:
**Stress Score = (Emotion × 0.4) + (Voice × 0.2) + (Behaviour × 0.2) + (Survey × 0.2)**

- **Low Stress (0.0 - 0.4)**: Positive feedback and motivational support.
- **Medium Stress (0.4 - 0.7)**: Breathing exercises, break reminders, and relaxation suggestions.
- **High Stress (0.7 - 1.0)**: Urgent interventions, AI study planner, and counselor alerts.

---

## 🛠️ Setup & Deployment Instructions

### 1. Prerequisites
- Python 3.9+
- MySQL Server
- A modern web browser with camera/mic access

### 2. Database Setup
1. Open your MySQL client (e.g., MySQL Workbench).
2. Run the `schema.sql` script to create the database and tables.
3. Update `app/config.py` with your MySQL credentials:
   ```python
   SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:YOUR_PASSWORD@localhost/stresssencs_db'
   ```

### 3. Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/StressSencsAI.git
   cd StressSencsAI
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 4. Running the Application
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   - Student App: `http://localhost:5000/`
   - Admin Dashboard: `http://localhost:5000/admin/dashboard`

---

## ✨ Features
- **Multimodal AI**: Combines visual, auditory, and behavioral data.
- **Real-time Detection**: Uses `navigator.mediaDevices` for camera/mic capture.
- **Personalized Guidance**: Dynamic interventions based on stress level.
- **Advanced Admin Panel**: Chart.js heatmaps and departmental stress trends.
- **Automated Alerts**: Email simulation for high-risk students.

---

## 👨‍💻 Developer Notes
For a final-year project, ensure you have the `emotion_model.h5` file in the `data/` folder. If not present, the system will use a mock predictor for demonstration purposes. To improve voice analysis, calibrate the pitch and tempo thresholds based on your target demographic.
