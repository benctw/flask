from flask import Flask, url_for, request, render_template, request, redirect
from markupsafe import escape

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
    return render_template('hello.html', name=name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['email'],
                       request.form['password']):
            return redirect(url_for('hello', name=request.form['email']))
        else:
            error = '帳號/密碼錯誤'
            return error
    else:
        return render_template('login.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
