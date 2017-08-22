from bs4 import BeautifulSoup
import requests

def spider_1(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')

    titles = soup.select('dd > p.title > a')            # 标题
    hrefs = soup.select('dd > p.title > a')            # 链接
    details = soup.select('dd > p.mt12')                # 建筑信息
    courts = soup.select('dd > p:nth-of-type(3) > a')   # 小区
    areas = soup.select('dd > div.area.alignR > p:nth-of-type(1)')     # 面积
    prices = soup.select('dd > div.moreInfo > p:nth-of-type(1) > span.price')  # 总价
    danjias = soup.select('dd > div.moreInfo > p.danjia.alignR.mt5')    # 单价


    for court,area, price, danjia, title, detail, href in zip(courts,areas,prices,danjias,titles,details, hrefs):
        data = {
            '小区': court.get_text(),
            '面积': area.get_text(),
            '总价': price.get_text(),
            '单价': danjia.get_text(),
            '标题': title.get_text(),
            '详细': list(detail.stripped_strings),
            '链接': 'http://esf.km.fang.com' + href.get('href'),
        }
        print(data)

# 循环，把第2-100页全部爬下来
page = 1
while page < 50:
    #url = 'http://esf.km.fang.com/house/i3'+str(page+1)
    #url = 'http://esf.km.fang.com/house/t21-h316-i3'+str(page+1)
    url = 'http://esf.km.fang.com/house/c280-d2200-j290-k2150-t21-h316-i3'+str(page+1)+'-l3110'
    spider_1(url)
    page = page + 1

'''
def Pages():
# 循环，把第2-100页全部爬下来
    page = 1
    a = {}
    while page < 1:
    #url = 'http://esf.km.fang.com/house/i3'+str(page+1)
    #毛坯+最新
    #url = 'http://esf.km.fang.com/house/t21-h316-i3'+str(page+1)
        url = 'http://esf.km.fang.com/house/c280-d2200-j290-k2150-t21-h316-i3'+str(page+1)+'-l3110'
        a = spider_1(url)
        page = page + 1
    print(a)
    return a

# 循环，把第2-100页全部爬下来
page = 1
while page < 10:
    #url = 'http://esf.km.fang.com/house/i3'+str(page+1)
    #毛坯+最新
    #url = 'http://esf.km.fang.com/house/t21-h316-i3'+str(page+1)
    url = 'http://esf.km.fang.com/house/c280-d2200-j290-k2150-t21-h316-i3'+str(page+1)+'-l3110'
    #a = spider_1(url)
    spider_1(url)
    page = page + 1

    csvFile3 = open('csvFile3.txt','a', newline='',encoding='gb18030')
    print(a)
    csvFile3.writelines(str(a))
    csvFile3.close()
'''
