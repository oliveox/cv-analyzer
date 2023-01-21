from flask import Flask, jsonify
import click

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


@app.cli.command("section")
@click.argument("name")
def get_cv_section_cli(name):
    result = get_section(name)
    print(result)


@app.route("/")
def index():
    return "Let's analyze your CV!"


@app.get('/personal')
def get_personal_section_api():
    result = get_section("personal")
    return jsonify(result)


@app.get('/experience')
def get_experience_section_api():
    result = get_section("experience")
    return jsonify(result)


@app.get('/education')
def get_education_section_api():
    result = get_section("education")
    return jsonify(result)


def get_section(section):
    try:
        return CV[section]
    except KeyError:
        return {
            "error": f"The CV doesn't contain an [{section}] section"
        }
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        return {
            "error": "Unexpected error"
        }
