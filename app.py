from flask import Flask, url_for, request, render_template, request, redirect, make_response, session, g
from markupsafe import escape
import time, pymysql, sqlite3

def valid_login(email, password):
    sql = f'select * from `user` where `email`="{email}" and `password`="{password}"'
    cursor = g.conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    return data if data else False

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.before_request
def before():
    g.user_email=''
    # 連接資料庫
    g.conn = sqlite3.connect('chatbot.db')

@app.teardown_request
def teardown(exception):
    # 關閉連線資源
    g.conn.close()

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
            session['user_email'] = request.form['email']
            g.user_email = request.form['email']
            return redirect(url_for('hello', name=request.form['email']))
        else:
            error = '帳號/密碼錯誤'
            return error
    else:
        if 'user_email' in session:
            return redirect(url_for('hello', name=session['user_email']))
        else:
            return render_template('login.html')
            
@app.route('/logout')
def logout():
    session.pop('user_email', None)
    g.user_email = ''
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
