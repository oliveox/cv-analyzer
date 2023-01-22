from flask import Flask, jsonify
import click

from src.cv import CV

app = Flask(__name__)


@app.cli.command("section")
@click.argument("name")
def get_cv_section_cli(name):
    """ Get a section from the CV """
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
            "error": f"The CV doesn't contain a section named [{section}] "
        }
    except Exception as e:
        print(f"Unexpected error occured: {e}")
        return {
            "error": "Unexpected error"
        }
