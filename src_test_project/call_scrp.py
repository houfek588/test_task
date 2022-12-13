import os
import json
import database

# os.system('scrapy crawl sreality -O sr1.json')

with open("sr1.json", encoding = 'utf-8') as f:

    file = json.loads(f.read())


SaveData = database.MyPostgreSQLData()

SaveData.delete_all()
for y in file:
    SaveData.insert_row(y['name'],y['link'])



print(SaveData.get_all())