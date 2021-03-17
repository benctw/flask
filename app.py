from flask import Flask, url_for, request, render_template, request, redirect, make_response
from markupsafe import escape
import time

def valid_login(email, password):
    if (email=='benctw@gmail.com' and password=='kk123'):
        return True
    else:
        return False

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
@app.route('/hello')
def hello(name=None):
    request_from_args = request.args.get('name','')
    if request_from_args: name=request_from_args
    return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['email'],
                       request.form['password']):
            resp = make_response(redirect(url_for('hello', name=request.form['email'])))
            resp.set_cookie('user_email', request.form['email'], expires=time.time()+60*60*24*7)
            return resp
        else:
            error = '帳號/密碼錯誤'
            return error
    else:
        user_email = request.cookies.get('user_email')
        if user_email:
            return redirect(url_for('hello', name=user_email))
        else:
            return render_template('login.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
