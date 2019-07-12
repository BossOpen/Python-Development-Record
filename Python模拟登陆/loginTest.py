# coding:utf-8
from bs4 import BeautifulSoup
import requests
"""Python模拟登陆QTCN。www.qtcn.org"""
# 设置登录url
login_url = "http://www.qtcn.org/bbs/login.php?"


# 创建登录类
class Login(object):
    # 初始化
    def __init__(self):
        # 用户名密码
        self.username = ''
        self.password = ''
        # 验证码
        # self.rode = ''
        # 用户代理模拟浏览器
        self.user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
        # session保存cookies
        self.session = requests.Session()
        headers = {'User-Agent': self.user_agent,
                   'Host': 'www.qtcn.org',
                   'Referer': 'http://www.qtcn.org/bbs/login.php',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Upgrade-Insecure-Requests': '1'
                   }

        self.session.headers.update(headers)
        return

    def set_login_info(self, user_name, user_password):
        """设置登录用户信息"""
        self.username = user_name
        self.password = user_password

    def login(self):
        """"模拟登录"""
        # wireshark抓取的浏览器登录数据
        login_data = {'jumpurl': 'http://www.qtcn.org/bbs/i.php',
                      'pwuser': self.username, 'pwpwd': self.password,
                      'step': 2, 'lgt': 0}

        # 需要给Post数据编码
        # login_data = urllib.urlencode(values)
        # 登录
        response = self.session.post(login_url, data=login_data)
        # print response.content

        # 通过BeautifulSoup获取网页内容
        soup = BeautifulSoup(response.content, 'lxml')
        # 获取网页的content
        data = soup.find_all(class_='f14 mb10')
        if data:
            print u'模拟登录成功!', data
        else:
            print u'模拟登录失败!'

    def skip(self, skip_url):
        # 模拟登录成功后,跳转网页
        # ----------------------------
        # 传递跳转网页的url
        headers = {'User-Agent': self.user_agent,
                   'Host': 'www.qtcn.org',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
        self.session.headers.update(headers)
        # 跳转
        response = self.session.get(skip_url)
        # print response.content
        soup = BeautifulSoup(response.content, 'lxml')
        # 获取跳转后网页的title
        print soup.title.string


if __name__ == "__main__":
    user_login = Login()
    username = '****************'
    password = '****************'
    user_login.set_login_info(username.decode('utf8').encode('gb2312'), password)
    # 执行模拟登录方法
    user_login.login()
    # 执行模拟登录成功后网页跳转方法
    user_login.skip(skip_url='http://www.qtcn.org/bbs/i.php')
