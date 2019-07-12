# coding:utf-8
"""
功能:爬取安居客新房信息
"""
import urllib2
import bs4

pages = ['p1/', 'p2/', 'p3/', 'p4/', 'p5/', 'p6/']
base_url = "http://cs.fang.anjuke.com/loupan/all/"
user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
headers = {'User-Agent': user_agent}

# 爬取结果存储
house_file = open('anjuke.txt', 'a+')

for obj in pages:
    url = base_url + obj
    print url
    # 向服务器发送访问请求
    req = urllib2.Request(url=url, headers=headers)
    # 打开读取服务器返回的html页面
    response = urllib2.urlopen(req)
    # 通过BeautifulSoup处理返回的页面
    soup = bs4.BeautifulSoup(response, 'lxml')
    # 获取房产信息
    data_list = soup.select('.item-mod')

    # 从data_list中获取详情数据
    house_list = []
    for data in data_list:
        house = []
        try:
            # 获取楼盘名称
            item_name = data.select('div[class="infos"] > a[class="lp-name"] > h3')
            if len(item_name) > 0:
                item = item_name[0].get_text()
                print item
                # house_file.write(item.encode('utf-8') + ':')

            # 获取楼盘状态
            rec_status = data.select('div[class="tag-panel"] > i')
            if len(rec_status) > 0:
                rec = rec_status[0].get_text()
                print rec
                # house_file.write(rec.encode('utf-8') + ',')

            # 获取楼盘地址
            address_list = data.select('div[class="infos"] > a[class="address"] > span')
            if len(address_list) > 0:
                address = address_list[0].get_text()
                print address
                # house_file.write(address.encode('utf-8') + ',')

            # 获取楼盘价格
            price_list = data.select('a[class="favor-pos"] > p[class="price"] > span')
            if len(price_list) > 0:
                price = price_list[0].get_text()
                print price
                # house_file.write(price.encode('utf-8') + '\n')

        except Exception as e:
            print e
