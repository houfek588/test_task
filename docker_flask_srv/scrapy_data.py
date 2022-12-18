import json
import database
import subprocess
import os
# import scrapy
# from scrapy.crawler import CrawlerProcess
# import scrapy_part.sreality.sreality.spiders.sreality as sp
# function to save data to database
def SaveSQLData():
    with open("scrapy_part/sreality/sr1.json", encoding = 'utf-8') as f:
        file = json.loads(f.read())

    saved_data = database.MyPostgreSQLData()
    saved_data.delete_all()

    for y in file:
        saved_data.insert_row(y['name'],y['link'])

    return 'DATA SAVED'

def StartScrapy():
    # os.system('dir')
    # os.system('cd ./scrapy_part/sreality')
    # os.system('dir')
    subprocess.run(["scrapy", "crawl", "sreality", "-o", "sr1.json"], cwd='scrapy_part/sreality')
    # class TestSpider(scrapy.Spider):
    #     name = 'sreality'

    # if __name__ == "__main__":
    #     process = CrawlerProcess()
    #     process.crawl(sp.SrealityTestProject)
    #     process.start()
    return 'SCRAPY STARTED'




