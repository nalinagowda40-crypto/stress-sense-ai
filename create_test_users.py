from app import create_app, db
from app.models.models import Student, User
from werkzeug.security import generate_password_hash

app = create_app()
app.app_context().push()

# Clear existing data (optional)
# db.session.query(Student).delete()
# db.session.query(User).delete()

# Create test student
student = Student(
    name="John Doe",
    email="student@university.edu",
    password_hash=generate_password_hash("student123"),
    department="Computer Science",
    year_of_study=2
)
db.session.add(student)

# Create test admin
admin = User(
    name="Admin User",
    email="admin@university.edu",
    password_hash=generate_password_hash("admin123"),
    role="admin"
)
db.session.add(admin)

db.session.commit()
print("✅ Test accounts created!")
print("\nTest Credentials:")
print("=" * 50)
print("STUDENT LOGIN:")
print("  Email: student@university.edu")
print("  Password: student123")
print("\nADMIN LOGIN:")
print("  Email: admin@university.edu")
print("  Password: admin123")
print("=" * 50)
