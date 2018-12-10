# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import lxml.html
from tmall.items import TmallItem

# headers = {
#     # "Cookie":"hng=CN%7Czh-CN%7CCNY%7C156; lid=%E9%9B%A82211977037; cna=cpTME8UkOkwCAXWfD92mmXL4; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; sm4=410100; tk_trace=1; t=b0132cbaf34a91fdf8ce22e37bcad3f3; tracknick=%5Cu96E82211977037; lgc=%5Cu96E82211977037; _m_h5_tk=1b570233583ec5b2f4f13b04fb6bbc3a_1542256613939; _m_h5_tk_enc=01e0268ec13d9c3dc43c0a8967e61145; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=VT5L2FSpccLuJBreK%2BBd&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTYNO0qGgZ8NA%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByR%2FCnDCfBSqvZBU%3D&id2=UojTVuIGBqxGwQ%3D%3D&nk2=sGo0FeQsn7tZPAQK&lg2=WqG3DMC9VAQiUQ%3D%3D; _l_g_=Ug%3D%3D; ck1=""; unb=1972453173; cookie1=BvHR0gEgzkjjTlbM%2BhYAoAhs5W88mELZExzZMnMWYik%3D; login=true; cookie17=UojTVuIGBqxGwQ%3D%3D; cookie2=1481d6fb3e034d9324803439d3ad4b84; _nk_=%5Cu96E82211977037; uss=""; csg=fbabfc62; skt=cd09d9baea8f7d81; _tb_token_=e85eb3417b167; enc=L8KPvBm7R5FaxrDdQxwk8eomVySQw9KjFs5UBtvAwjOBqFol0hDg6ReVqPYwZzJHPC9doAvSVqcpmleMCnZXLQ%3D%3D; cq=ccp%3D0; swfstore=16091; x=__ll%3D-1%26_ato%3D0; pnm_cku822=098%23E1hvCvvUvbpvU9CkvvvvvjiPR2qU6j18PL591jthPmPv1jnmRLLytjlEPsdhQj3PR2K5vpvhvvmv99hCvvOvCvvvphvEvpCWvU3tvvw0TWex6fItb9TxfwCl5dUfbj7QD70fd56OfwCl%2Bb8rwos6D7zhdiZDNr1l%2BE7rVC69kjjxQCy1wkqxQWkXemglCwkXAjVTVbyCvm9vvvvUphvvPpvv9FCvpv3bvvv2vhCv2UhvvvWvphvWgvvv9FavpvAykphvC99vvOC0LTyCvv9vvUmsxZI6UpGCvvLMMQvvRphvCvvvvvv%3D; whl=-1%260%260%260; isg=BM_PAcldyCp5ksx1yed3Y2oAXmPT_LorfFYY1OHdzD4VsO6y6cYfZ4VitqCryPuO",
#     "Cookie":"hng=CN%7Czh-CN%7CCNY%7C156; lid=%E9%9B%A82211977037; cna=cpTME8UkOkwCAXWfD92mmXL4; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; sm4=410100; tk_trace=1; t=b0132cbaf34a91fdf8ce22e37bcad3f3; tracknick=%5Cu96E82211977037; lgc=%5Cu96E82211977037; _m_h5_tk=1b570233583ec5b2f4f13b04fb6bbc3a_1542256613939; _m_h5_tk_enc=01e0268ec13d9c3dc43c0a8967e61145; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=VT5L2FSpccLuJBreK%2BBd&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTYNO0qGgZ8NA%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dByR%2FCnDCfBSqvZBU%3D&id2=UojTVuIGBqxGwQ%3D%3D&nk2=sGo0FeQsn7tZPAQK&lg2=WqG3DMC9VAQiUQ%3D%3D; _l_g_=Ug%3D%3D; ck1=""; unb=1972453173; cookie1=BvHR0gEgzkjjTlbM%2BhYAoAhs5W88mELZExzZMnMWYik%3D; login=true; cookie17=UojTVuIGBqxGwQ%3D%3D; cookie2=1481d6fb3e034d9324803439d3ad4b84; _nk_=%5Cu96E82211977037; uss=""; csg=fbabfc62; skt=cd09d9baea8f7d81; _tb_token_=e85eb3417b167; enc=L8KPvBm7R5FaxrDdQxwk8eomVySQw9KjFs5UBtvAwjOBqFol0hDg6ReVqPYwZzJHPC9doAvSVqcpmleMCnZXLQ%3D%3D; cq=ccp%3D0; swfstore=16091; x=__ll%3D-1%26_ato%3D0; pnm_cku822=098%23E1hvxpvUvbpvUvCkvvvvvjiPR2qUljiWP2sv6jEUPmP9QjrmnLLOtjYRnLzZljDPiQhvCvvvpZptvpvhvvCvpvGCvvpvvPMMKphv8vvvpjyvvv2CvvCHEpvvv7yvvhXVvvmCWvvvByOvvUhwvvCH8Qvv9XoivpvUvvCCEDBrfHeEvpvVvpCmpYFymphvLvb0uuIa9b8re4tYVVzheug7%2B3%2Butj7JyC978BLOzCuwHF%2BSBiVvVE01%2B2n79RvaRfUTnZJt9b8rV8tYVVzhdi7Adc9D%2BE7rj8TJOFGCvpvVvUCvpvvv; whl=-1%260%260%260; isg=BH19GDfA-nDPqV6_t5kFCSzGjNl9EihRelAqnj_CbVQDdp2oB2gpPRfkJOqVdskk",
#     "Referer":"https://list.tmall.com/search_shopitem.htm?spm=a220m.1000858.1000725.2.19bdadbfB6iW5M&user_id=2560660690&from=_1_&stype=search"
# }


class EveSpider(scrapy.Spider):
    name = 'eve'
    # allowed_domains = ['detail.tmall.com']

    def start_requests(self):
        base_url = "https://detail.tmall.com/item.htm?spm=a220m.1000858.1000725.1.10071a2e3E99KN&id=576412995625&skuId=3959303342392&areaId=410881&standard=1&user_id=533497499&cat_id=50029231&is_b=1&rn=297f6b58b52879a5dd9d1a7b4d628f85"
        yield Request(url=base_url,callback=self.parse,dont_filter=True,meta={"page":"1"})

    def parse(self, response):
        item = TmallItem()
        tr_list = response.xpath('//div[@class="rate-grid"]/table/tbody/tr').extract()
        for tr in tr_list:
            html = lxml.html.fromstring(tr)
            try:
                command = html.xpath('//div[@class="tm-rate-premiere"]/div[@class="tm-rate-content"]/div[@class="tm-rate-fulltxt"]/text()')[0]
            except:
                try:
                    command = html.xpath('//div[@class="tm-rate-content"]/div[@class="tm-rate-fulltxt"]/text()')[0]
                except:
                    command = "此用户暂无评价"
            times = html.xpath('//div[@class="tm-rate-date"]/text()')[0]
            try:
                explain = html.xpath('//div[@class="tm-rate-reply"]/div[@class="tm-rate-fulltxt"]/text()')[0]
            except:
                explain = "暂无店家解释"
            try:
                grade = html.xpath('//div[@class="rate-user-grade"]/p/text()')[0]
            except:
                grade = "普通会员"
            try:
                append_command = html.xpath('//div[@class="tm-rate-append"]/div[@class="tm-rate-content"]/div[@class="tm-rate-fulltxt"]/text()')[0]
            except:
                append_command = "暂无追加评论"
            item["command"] = command
            item["times"] = times
            item["explain"] = explain
            item["grade"] = grade
            item["append_command"] = append_command
            yield item

        yield Request(url="http://www.baidu.com",callback=self.parse,meta={"page":"2"},dont_filter=True)




