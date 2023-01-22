### Retrieve CV data using REST API or CLI

## Instructions
- You can use `python` / `python3` and `pip` / `pip3` interchangeably, depending on your system configuration
- API server and CLI commands are accessible from everywhere in the current shell, as long as the virtual environment is activated and the `FLASK_APP` environment variable is set

### Requirements
- Python 3: `python3 --version` 
- pip: `pip --version`

### Install
1. `git clone` repository
2. `cd` into the repository
3. create virtual environment: `python3 -m venv venv`
4. activate virtual environment: `source venv/bin/activate`
5. install package: `pip install .`

### Start the REST API server
1. activate virtual environment: `source venv/bin/activate`
2. export environment variable: `export FLASK_APP=src.app`. With the virtual environment activated, it allows running the API server from anywhere, in the current shell
3. start server: `flask run`
4. server listens at http://127.0.0.1:5000. Available API's:
    - GET `/personal`
    - GET `/experience`
    - GET `/education`
5. `Ctrl + C` to stop the server

### Execute the CLI command
1. activate virtual environment: `source venv/bin/activate`
2. export environment variable: `export FLASK_APP=src.app`. With the virtual environment activated, it allows running the CLI command from anywhere, in the current shell
3. run CLI command: `flask section {section_name}`. E.g. `flask section education`
