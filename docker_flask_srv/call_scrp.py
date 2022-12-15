
import json
import database

# os.system('scrapy crawl sreality -O sr1.json')
def SaveSQLData():
    with open("scrapy_part/sreality/sr1.json", encoding = 'utf-8') as f:
        file = json.loads(f.read())

    saved_data = database.MyPostgreSQLData()

    saved_data.delete_all()
    for y in file:
        saved_data.insert_row(y['name'],y['link'])

    print(saved_data.get_all())
    return 'done'

# SaveSQLData()