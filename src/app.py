from flask import Flask, jsonify

app = Flask(__name__)

CV = {
    "personal": [
        {"year": "1990", "name": "John Doe"},
    ],
    "experience": [
        {"year": "2020 - 2023", "company": "Google"},
        {"year": "2023 - Present", "company": "Cegeka"},
    ],
    "education": [
        {"year": "2010 - 2014", "school": "High-School"},
        {"year": "2014 - 2018", "school": "MIT"},
    ],
}


@app.route("/")
def index():
    return "Let's analyze your CV!"


@app.get('/personal')
def get_personal_section():
    try:
        return jsonify(CV['personal'])
    except KeyError:
        return jsonify({
            "error": "The CV doesn't contain an [personal] section"
        })
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        return jsonify({
            "error": "Unexpected error"
        })


@app.get('/experience')
def get_experience_section():
    try:
        return jsonify(CV['experience'])
    except KeyError:
        return jsonify({
            "error": "The CV doesn't contain an [experience] section"
        })
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        return jsonify({
            "error": "Unexpected error"
        })


@app.get('/education')
def get_education_section():
    try:
        return jsonify(CV['education'])
    except KeyError:
        return jsonify({
            "error": "The CV doesn't contain an [education] section"
        })
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        return jsonify({
            "error": "Unexpected error"
        })
