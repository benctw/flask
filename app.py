from flask import Flask  
app = Flask(__name__)  

# 鉤子函數  
@app.before_request  
def before():  
    print('before request!')  
 
@app.before_request  
def before():  
    print('before request!2')  
  
# 第一次調用時才會被執行  
@app.before_first_request  
def before():  
    print('before first!!!')  
 
@app.route('/index/')  
def index():  
    # 1/0  # 如果取消這裡的注釋after_request就不會執行了  
    return 'index'  

# 程式在不出異常才會被調用  
@app.after_request  
def after(response):  
    print('after request')  
    return response  
 
@app.after_request  
def after(response):  
    print('after request2')  
    return response  
 
@app.teardown_request  
def teardown(exception):  
    print('teardown request')  
  
if __name__ == '__main__':  
    app.run()