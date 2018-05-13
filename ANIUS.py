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

    '''
    === Get all the sites URL in document ===
    '''
    with open("Brand/ANIUS.txt") as brandURL:
        read = brandURL.readlines()
        numURL = len(read)
    print "There are %d pages" % (numURL)
    # print type(read)
    # for i in read:
    #     # print i + '\n'
    #     after = i.replace("?", "/?")
    #     print after
    for i in read:
        categoryNum = i[44:]
        # while():
        #     ...


    while True:
        # for element in range(numURL):

        '''
        === Preprocedure ===
        # URL example
        Original -> https://www.cango-shop.com/product?category=81
        Actually -> https://www.cango-shop.com/product/?category=81&page=1
        '''
        target = requests.get("https://www.cango-shop.com/product/?category=112&page=%s" % str(page))
        # target = requests.get("https://www.cango-shop.com/product/?category=%s&page=%s" % str(category) % str(page))
        target.encoding = 'utf8'
        root = etree.fromstring(target.text, etree.HTMLParser())
        # series = "="*5 + str(root.xpath('//*[@id="main"]/div/h1/text()')).decode("unicode-escape").encode("utf-8") + "="*5
        # seriesName = series.replace("[u\'", "").replace("\', \'", " : ").replace("']", "") + '\n'
        # print seriesName
        item = root.xpath('//*[@id="main"]/div/section/div/div/header/a[@class="de_remove-link-color"]/h3/text()')
        price = root.xpath('//*[@id="main"]/div/section/div/div/header/div/h3/text()')

        '''
        === Get all the product series in site ===
        '''
        while(boolSeries == False):
            series = "="*5 + str(root.xpath('//*[@id="main"]/div/h1/text()')).decode("unicode-escape").encode("utf-8") + "="*5
            seriesName = series.replace("[u\'", "").replace("\', \'", " : ").replace("']", "")
            print seriesName
            boolSeries = True

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
        with open("Prices/ANIUS.txt", "a+") as ANIUS_price:
            while(boolSeries == True):
                ANIUS_price.write(seriesName + '\n')

            for i in result:
                tmp = str(i).decode("unicode-escape").encode("utf-8")
                content = tmp.replace("(u\'", "").replace("\', \'", " : ").replace("')", "") + '\n'
                if("('" in content):
                    content = content.strip("('")
                else:
                    pass
                ANIUS_price.write(content)
            ANIUS_price.close()
            print "Page [ %s ] finish !" % num
        num += 1
        # print "XXX series done!"

if __name__ == "__main__":
    main(sys.argv)