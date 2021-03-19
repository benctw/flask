from flask import Flask, url_for, request, render_template, redirect, make_response, g
from markupsafe import escape
import time, sqlite3

def do_the_login(email, password):
    sql = f'select * from `user` where `email`="{email}" and `password`="{password}"'
    cursor = g.conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return data if data else False

app = Flask(__name__)

@app.before_request
def before():
    g.user_email=''
    # 連接資料庫
    g.conn = sqlite3.connect('flaskdb.db')

@app.teardown_request
def teardown(exception):
    # 關閉連線資源
    g.conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if do_the_login(email, password):
            resp = make_response(redirect(url_for('hello', useremail=email)))
            resp.set_cookie('useremail', email, expires = time.time()+60*60*24*7)
            return resp
        else:
            return redirect(url_for('error', errorcode=6000))
    else:
        if request.cookies.get('useremail'):
            return redirect(url_for('hello', useremail=request.cookies.get('useremail')))
        else:
            return render_template('login.html')

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('success', successcode=3001)))
    resp.set_cookie('useremail', '', expires=0)
    return resp

@app.route('/hello')
def hello():
    useremail = request.args.get('useremail', '')
    return render_template('hello.html', useremail=useremail)

@app.route('/success/<int:successcode>')
def success(successcode):
    return render_template('success.html', successcode=successcode)

@app.route('/error/<int:errorcode>')
def error(errorcode):
    return render_template('error.html', errorcode=errorcode)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
