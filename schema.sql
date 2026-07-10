CREATE DATABASE IF NOT EXISTS campusmind_db;
USE campusmind_db;

-- Students table
CREATE TABLE IF NOT EXISTS Students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(50),
    year_of_study INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- BehaviourLogs table
CREATE TABLE IF NOT EXISTS BehaviourLogs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    typing_speed FLOAT,
    hesitation_rate FLOAT,
    error_rate FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- EmotionRecords table
CREATE TABLE IF NOT EXISTS EmotionRecords (
    emotion_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    emotion_label VARCHAR(20),
    confidence_score FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- SurveyResponses table
CREATE TABLE IF NOT EXISTS SurveyResponses (
    survey_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    q1_score INT, -- Scale 1-5
    q2_score INT,
    q3_score INT,
    q4_score INT,
    q5_score INT,
    total_survey_score FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- StressScores table
CREATE TABLE IF NOT EXISTS StressScores (
    score_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    emotion_component FLOAT,
    voice_component FLOAT,
    behaviour_component FLOAT,
    survey_component FLOAT,
    total_stress_score FLOAT,
    stress_level ENUM('Low', 'Medium', 'High'),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Alerts table
CREATE TABLE IF NOT EXISTS Alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    alert_type VARCHAR(50),
    message TEXT,
    is_resolved BOOLEAN DEFAULT FALSE,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);

-- Recommendations table
CREATE TABLE IF NOT EXISTS Recommendations (
    rec_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    rec_type VARCHAR(50), -- 'StudyPlanner', 'Breathing', 'BreakReminder', etc.
    content TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES Students(student_id)
);
