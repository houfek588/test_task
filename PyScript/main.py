from flask import Flask,request
import database

MyData = database.MyPostgreSQLData()
names = MyData.get_all()

app = Flask(__name__)

@app.route('/')
def index():
    title = '<h1>HTML Python server</h1>'
    a = title
    # for i in range(0,5): a += '<p>ID: ' + str(names[i]) + '</p>'
    a += write_database()
    return a

def write_database():
    b = ''
    for n in names: b += f'<p>ID {n[0]}: {n[1]} {n[2]}</p>'
    return b


@app.route('/ja')
def ja():
    return 'Tvůj prohlížeč je ' + request.headers['user-agent']                 # vrátí prohližec

app.run(port=8080)

