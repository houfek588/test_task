import scrapy


class SrcTestProject(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/hledani/prodej/domy']

    # start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        # yield response.css('h1.page-title.list-title.ng-binding').get()
        for products in response.css('div.property.ng-scope'):
            # yield products.css('span.name.ng-binding').get()
            # try:
            yield {
                'name': products.css('span.locality.ng-binding').get(),
                'price': products.css('span.price.ng-scope').get(),
            }
        # except:
        #     yield {
        #         'name': 'no product',
        #
        #     }
