from flask import Flask, url_for, request
from markupsafe import escape

def do_the_login():
    return "do_the_login"

def show_the_login_form():
    return "show_the_login_form"

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
