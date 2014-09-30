from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem

class MySpider(BaseSpider):
  name = "craig"
  allowed_domains = ["craigslist.org"]
  start_urls = ["http://longisland.craigslist.org/search/sss?sort=date&query"]

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    rows = hxs.select('//div[@class="content"]/p[@class="row"]')

    items = []
    for row in rows:
        item = CraigslistSampleItem()
        link = row.xpath('.//span[@class="pl"]/a')
        item ['date'] = row.xpath('.//span[@class="pl"]/span[@class="date"]/text()').extract()
        item['title'] = link.xpath("text()").extract()
        item['link'] = link.xpath("@href").extract()
        item['price'] = row.xpath('.//span[@class="l2"]/span[@class="price"]/text()').extract()
        items.append(item)
    return items