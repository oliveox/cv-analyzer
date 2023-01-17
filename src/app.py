from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Let's analyze your CV!"

@app.route('/personal')
def get_personal_section():
    return 'personal section'

@app.route('/experience')
def get_experience_section():
    return 'experience section'

@app.route('/education')
def get_education_section():
    return 'education section'
