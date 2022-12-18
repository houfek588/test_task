from flask import Flask
import scrapy_data
import database

# MyData = database.MyPostgreSQLData()
# names = MyData.get_all()

app = Flask(__name__)

# home page function
@app.route('/')
def index():
    title = '<h1>HTML Python server</h1>'
    create_database()

    save_data()

    page_text = title
    page_text += write_database()
    return page_text

def write_database():
    my_data = database.MyPostgreSQLData()
    names = my_data.get_all()

    page_text = ''
    for n in names:
        page_text += f'<p>ID {n[0]}: {n[1]}</p>'
        page_text += f'<img src="{n[2]}">'
    return page_text

def create_database():
    my_data = database.MyPostgreSQLData()
    my_data.create_table()

def save_data():
    message = scrapy_data.SaveSQLData()
    return (f'<h1>{message}</h1>')

@app.route('/readme')
def readme():
    return ('<h1>readme page</h1>')
    # return ('<h1>readme page</h1>' + write_database())


# save data function
@app.route('/start_scrp')
def start_scrp():
    message = scrapy_data.StartScrapy()
    return (f'<h1>{message}</h1>')                 # vrátí prohližec


# app.run(port=80)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)