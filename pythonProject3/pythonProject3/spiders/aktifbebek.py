import scrapy
from ..items import Pythonproject3Item
class aktifBebek(scrapy.Spider) :
    name = 'aktifbebek'
    pageNumber = 1
    start_urls = [
        'https://www.aktifbebek.com/bebek-bakimi-ve-banyo'
    ]

    def parse(self, response):
        items=PythonprojectItem()
        products=response.xpath("//div[@class='products-item']").getall()

        for product in products:
            productName= response.xpath("//a[@class='name']/text()").get()
            print("productName",productName)
            brand=product.xpath("//a[@class='brand']/text()").get()
            print("brand",brand)
            barcode=product.xpath("p/text()").get()
            print("barcode",barcode)
            image=product.xpath("//img/@data-src").get()
            print("image",image)
            productUrl= response.xpath("//a[@class='name']/@href").get()
            items["name"]=productName
            items["brand"]=brand
            items["image"]=image
            items["url"]=productUrl
            #print("ITEMS",items)
        yield items

        if aktifBebek.pageNumber<3 :
            print("pageNumber:",aktifBebek.pageNumber)
            aktifBebek.pageNumber += 1
            next_page='https://www.aktifbebek.com/bebek-bakimi-ve-banyo?Kategori=13&sayfa='+str(aktifBebek.pageNumber)
            print("next_Page",next_page)
            yield response.follow(url=next_page, callback=self.parse)







