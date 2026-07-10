import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', message='.*numpy.*')

from app import create_app, db
from app.models.models import Student, BehaviourLog, EmotionRecord, SurveyResponse, StressScore, Alert, Recommendation

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Student': Student,
        'BehaviourLog': BehaviourLog,
        'EmotionRecord': EmotionRecord,
        'SurveyResponse': SurveyResponse,
        'StressScore': StressScore,
        'Alert': Alert,
        'Recommendation': Recommendation
    }

if __name__ == '__main__':
    # Automatically initialize the database test records
    with app.app_context():
        try:
            from init_db import init_db
            init_db()
        except BaseException as e:
            print("Auto-init info:", e)

    app.run(host='localhost', port=5000, debug=True)
