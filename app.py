from flask import Flask, url_for, request, render_template
from markupsafe import escape

def do_the_login():
    return "do_the_login"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
