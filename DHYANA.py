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
    with open("Brand/DHYANA.txt") as brandURL:
        read = brandURL.readlines()
        numURL = len(read)
        # print numURL
        for i in read:
            # print i
            url = i
            target = requests.get("%s" % url)
            target.encoding = 'utf8'
            root = etree.fromstring(target.text, etree.HTMLParser())
            item = root.xpath('//*/h1/text()')
            price = root.xpath('//*[@id="hw_size"]/option/text()')

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
            with open("Prices/DHYANA.txt", "a+") as DHYANA_price:
                while(boolSeries == True):
                    DHYANA_price.write(seriesName + '\n')

                for i in result:
                    tmp = str(i).decode("unicode-escape").encode("utf-8")
                    content = tmp.replace("(u\'", "").replace("\', \'", " : ").replace("')", "") + '\n'
                    if("('" in content):
                        content = content.strip("('")
                    elif("å" in content):
                        content = ''.join(content.rpartition('å')[:1]).replace("/", "/NT$")
                    else:
                        pass
                    DHYANA_price.write(content + '\n')
                DHYANA_price.close()
                break
            #     print "Page [ %s ] finish !" % num
            # num += 1

if __name__ == "__main__":
    main(sys.argv)