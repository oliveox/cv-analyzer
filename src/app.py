from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Let's analyze your CV!"

@app.get('/personal')
def get_personal_section():
    return 'personal section'

@app.get('/experience')
def get_experience_section():
    return 'experience section'

@app.get('/education')
def get_education_section():
    return 'education section'