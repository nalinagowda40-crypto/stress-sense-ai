#!/usr/bin/env python
"""Initialize the database and add test users"""

import warnings
warnings.filterwarnings('ignore')

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from app import create_app, db
from app.models.models import Student, User
from werkzeug.security import generate_password_hash
from datetime import datetime

def init_db():
    """Create all database tables"""
    app = create_app()
    
    with app.app_context():
        # Drop all tables (for fresh start)
        print("Creating database tables...")
        db.create_all()
        print("[OK] Database tables created")
        
        # Add test student if not exists
        if not Student.query.filter_by(email='student@university.edu').first():
            student = Student(
                name='John Doe',
                email='student@university.edu',
                password_hash=generate_password_hash('student123'),
                department='Computer Science',
                year_of_study=2,
                created_at=datetime.utcnow()
            )
            db.session.add(student)
            print("[OK] Test student account created")
        
        # Add test admin if not exists
        if not User.query.filter_by(email='admin@university.edu').first():
            admin = User(
                name='Admin User',
                email='admin@university.edu',
                password_hash=generate_password_hash('admin123'),
                role='admin',
                is_active=True,
                created_at=datetime.utcnow()
            )
            db.session.add(admin)
            print("[OK] Test admin account created")
        
        # Add more test students
        test_students = [
            ('sarah@university.edu', 'Sarah Smith', 'Engineering'),
            ('mike@university.edu', 'Mike Johnson', 'Business'),
            ('emma@university.edu', 'Emma Wilson', 'Medicine'),
        ]
        
        for email, name, dept in test_students:
            if not Student.query.filter_by(email=email).first():
                student = Student(
                    name=name,
                    email=email,
                    password_hash=generate_password_hash('password123'),
                    department=dept,
                    year_of_study=1,
                    created_at=datetime.utcnow()
                )
                db.session.add(student)
                print(f"[OK] Created test student: {name}")
        
        db.session.commit()
        print("\n[SUCCESS] Database initialization complete!\n")
        print("Test Accounts:")
        print("   Student Login: student@university.edu / student123")
        print("   Admin Login: admin@university.edu / admin123")
        print("\nStart the app with: python app.py")

if __name__ == '__main__':
    init_db()
