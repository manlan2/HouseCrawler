from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib

def spider_2(url):
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    html = opener.open(url)
    soup = BeautifulSoup(html, 'lxml')

    courts =  soup.find_all('span',class_='comm-address') #小区
    prices = soup.find_all('span',class_='price-det')#价格
    danjias = soup.find_all('span',class_='unit-price') #单价
    details = soup.find_all('div',class_='house-details')#其他
    titles = soup.find_all('a',class_='houseListTitle')#标题
    hrefs = soup.find_all('a',class_='houseListTitle') # 链接

    for court,price, danjia,detail,title, href in zip(courts,prices,danjias,details,titles, hrefs):
        data = {
            '小区': court.get_text(),
            '总价': price.get_text(),
            '单价': danjia.get_text(),
            '详细': detail.contents[3].get_text(),
            '标题': title.get('title'),
            '链接': href.get('href'),
        }
        print(data)

# 循环，把第2-100页全部爬下来
page = 1
while page < 1:
    #url = 'http://esf.km.fang.com/house/i3'+str(page+1)
    #url = 'http://esf.km.fang.com/house/t21-h316-i3'+str(page+1)
    url = 'https://km.anjuke.com/sale/d119-o5-p'+str(page+1) +'/?from_price=80&to_price=200&from_area=80&to_area=150'
    spider_2(url)
    page = page + 1


