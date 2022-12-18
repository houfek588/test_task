# import os
# import json
# import database

# os.system('scrapy crawl sreality -O sr1.json')

# with open("sr1.json", encoding = 'utf-8') as f:
#
#     file = json.loads(f.read())
#
#
# SaveData = database.MyPostgreSQLData()
#
# SaveData.delete_all()
# for y in file:
#     SaveData.insert_row(y['name'],y['link'])
# import scrapy
# from scrapy.crawler import CrawlerProcess
#
# class TestSpider(scrapy.Spider):
#     name = 'sreality'
#
# if __name__ == "__main__":
#   process = CrawlerProcess()
#   process.crawl(TestSpider)
#   process.start()


# print(SaveData.get_all())

import subprocess

subprocess.run(["scrapy", "crawl", "sreality", "-o", "quotes_all.json"])