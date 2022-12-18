import scrapy
# from scrapy_selenium import SeleniumRequest
from scrapy_splash import SplashRequest
from scrapy_splash.utils import to_native_str



class SrealityTestProject(scrapy.Spider):
    name = 'sreality'
    # start_urls = ['https://www.sreality.cz/hledani/prodej/byty']


    def start_requests(self):
        print('-------------------- Start Request ------------------------')

        yield SplashRequest(
            url=to_native_str('https://www.sreality.cz/hledani/prodej/byty/js'),
            callback=self.parse,
            endpoint='render.json'
        )


    def parse(self, response):

        print('----------------------------- PARSE ----------------------------------')
        print(response.url)

        # self.start_requests()
        # print(response.text)

        for products in response.css('div.property.ng-scope'):
             # self.index += 1
             # if self.index > 500: break

             yield {
                 'name': products.css('span.name.ng-binding::text').extract_first(),
                 'link': products.css('img').attrib['src'].extract(),
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


