import scrapy
from scrapy_selenium import SeleniumRequest

# g_act_link = 'https://www.sreality.cz/hledani/prodej/byty'

class SrealityTestProject(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/hledani/prodej/byty']

    # self.act_link = 'https://www.sreality.cz/hledani/prodej/byty'

    def start_requests(self):
        self.index = 0
        print('-------------------- SeleniumRequest ------------------------')
        yield SeleniumRequest(
            url="https://www.sreality.cz/hledani/prodej/byty",
            # url=g_act_link,
            wait_time=3,
            screenshot=True,
            callback=self.parse,
            dont_filter=True
        )

    def parse(self, response):

        print('----------------------------- PARSE ----------------------------------')
        print(response.url)
        # print(response.text)
        self.start_requests()

        for products in response.css('div.property.ng-scope'):
             self.index += 1
             # if self.index > 500: break

             yield {
                 'name': products.css('span.name.ng-binding::text').get(),
                 'link': products.css('img').attrib['src'],
             }

        # if self.index > 500:
        #     pass
        # else:
        #     print('------------------- NEXT PAGE ------------------------')
        #     next_page = 'https://www.sreality.cz' + response.css('a.btn-paging-pn.icof.icon-arr-right.paging-next').attrib['href']
        #     print(next_page)
        #     g_act_link = next_page
        #     print(g_act_link)
        #     print('------------------------------------------------------')
        #     if next_page is not None:
        #         yield response.follow(next_page, method='POST', callback=self.parse)


