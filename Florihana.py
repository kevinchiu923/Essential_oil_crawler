# !/usr/bin/env python
# _*_ coding: utf8 _*_

from lxml import etree
import requests
import sys
import re

def main(argv):
    page        = 1
    num         = 1
    numURL      = 1
    boolSeries  = False
    while True:
        '''
        === Get all the sites URL in document ===
        '''
        with open("Brand/Florihana.txt") as brandURL:
            read = brandURL.readlines()
            numURL = len(read)
        for i in read:
            url = i

            target = requests.get("%s" % url) 
            target.encoding = 'utf8'
            root = etree.fromstring(target.text, etree.HTMLParser())
            item = root.xpath('//*[@id="cate-page"]/div/div/div/div/div/div/div/div/a/h3/text()')
            price = root.xpath('//*[@id="cate-page"]/div/div/div/div/div/div/div/div/div/text()')

            '''
            === Ready to crawl the products - Name, capacity and price ===
            '''

            result       = []
            combineItem  = []
            combinePrice = []

            if len(item) == 0:
                break
            else:
                for item in item:
                    combineItem.append(item)

                for price in price:
                    price = price.encode('utf-8').strip()
                    combinePrice.append(price)

                page+=1
            result = zip(combineItem, combinePrice)

            '''
            === Save the records ===
            '''
            with open("Prices/Florihana.txt", "a+") as Florihana_price:
                while(boolSeries == True):
                    Florihana_price.write(seriesName + '\n')

                for i in result:
                    tmp = str(i).decode("unicode-escape").encode("utf-8")
                    content = tmp.replace("(u\'", "").replace("\', \'", " : ").replace("')", "") + '\n'
                    if("('" in content):
                        content = content.strip("('")
                    elif("å" in content):
                        content = ''.join(content.rpartition('å')[:1])
                    else:
                        pass
                    Florihana_price.write(content + '\n')
                Florihana_price.close()

if __name__ == "__main__":
    main(sys.argv)