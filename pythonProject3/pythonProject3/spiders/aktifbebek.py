import scrapy
from ..items import Pythonproject3Item
class aktifBebek(scrapy.Spider) :
    name = 'aktifbebek'
    pageNumber = 1
    start_urls = [
        'https://www.aktifbebek.com/bebek-bakimi-ve-banyo'
    ]

    def parse(self, response):
        items=Pythonproject3Item()
        productsList=response.xpath("//div[@class='products-list']")
        productsItem=productsList.xpath("//div[@class='products-item']")

        print("productItem: ", aktifBebek.pageNumber,"  ","len: ",len(productsItem),productsItem.extract())

        for product in productsItem:
            print("product beyza","page:", aktifBebek.pageNumber, product.extract())
            productName= product.css('a[class*=name] ::text').get()
            print("productName mehmet",productName)
            brand=product.css('a[class*=brand] ::text').get()
            print("brand me ",brand)
            barcode=product.css("p::text").get()
            print("barcode meh",barcode)
            image=product.css('img::attr(data-src)').get()
            print("image mehm",image)
            productUrl= response.css("a[class*=name] ::attr(href)").get()

            items["name"]=productName
            items["brand"]=brand
            items["image"]=image
            items["barcode"]=barcode
            items["url"]=productUrl
            yield items

        if aktifBebek.pageNumber<3 :
            print("pageNumber:",aktifBebek.pageNumber)
            aktifBebek.pageNumber += 1
            next_page='https://www.aktifbebek.com/bebek-bakimi-ve-banyo?Kategori=13&sayfa='+str(aktifBebek.pageNumber)
            print("next_Page",next_page)
            yield response.follow(url=next_page, callback=self.parse)