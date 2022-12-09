from flask import Flask,request
import random

app = Flask(__name__)

@app.route('/')
def index():
    title = '<h1>list</h1>'
    a = title
    for i in range(0,10): a += '<p>' + str(i) + '</p>'

    return str(a)


@app.route('/ja')
def ja():
    return 'Tvůj prohlížeč je ' + request.headers['user-agent']                 # vrátí prohližec

app.run(port=8080)

