from flask import Flask, escape, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Welcome here!'

@app.route('/user/<name>')
def user_name(name):    
    return 'Welecome %s' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('user_name', name='lizheng'))
    return 'Test page'