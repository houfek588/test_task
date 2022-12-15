from flask import Flask
import call_scrp
import database

MyData = database.MyPostgreSQLData()
names = MyData.get_all()

app = Flask(__name__)

@app.route('/')
def index():
    title = '<h1>HTML Python server</h1>'
    a = title
    # for i in range(0,5): a += '<p>ID: ' + str(names[i]) + '</p>'
    # a += write_database()
    return a

def write_database():

    # my_data = database.MyPostgreSQLData()
    # names = my_data.get_all()
    # names = [(20,'byt01','http'),(21,'byt02','httppp'),(22,'byt02','httttp')]
    b = ''
    for n in names:
        b += f'<p>ID {n[0]}: {n[1]}</p>'
        b += f'<img src="{n[2]}">'
    return b


@app.route('/readme')
def readme():
    # return 'Tvůj prohlížeč je ' + request.headers['user-agent']                 # vrátí prohližec
    return ('<h1>readme page</h1>' + write_database())

@app.route('/save')
def save():
    message = call_scrp.SaveSQLData()
    return ('<h1>SQL data saved</h1>' + message)                 # vrátí prohližec


# app.run(port=80)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')