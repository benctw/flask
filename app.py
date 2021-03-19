from flask import Flask, url_for, request, render_template
from markupsafe import escape

def do_the_login(email, password):
    if email=='benctw@gmail.com' and password=='kk123':
        return "登入成功"
    else:
        return "登入失敗"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email)
        print(password)
        return do_the_login(email, password)
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
