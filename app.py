from flask import Flask, url_for, request, render_template, redirect, make_response
from markupsafe import escape
import time

def do_the_login(email, password):
    if email=='benctw@gmail.com' and password=='kk123':
        resp = make_response(redirect(url_for('hello', useremail=email)))
        resp.set_cookie('useremail', email, expires = time.time()+60*60*24*7)
        return resp
    else:
        return redirect(url_for('error', errorcode=6000))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return do_the_login(email, password)
    else:
        if request.cookies.get('useremail'):
            return redirect(url_for('hello', useremail=request.cookies.get('useremail')))
        else:
            return render_template('login.html')


@app.route('/hello')
def hello():
    useremail = request.args.get('useremail', '')
    return f'Hello, {useremail}'

@app.route('/error/<int:errorcode>')
def error(errorcode):
    return render_template('error.html', errorcode=errorcode)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
