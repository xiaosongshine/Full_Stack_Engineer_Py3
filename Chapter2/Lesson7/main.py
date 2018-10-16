"""
Py2.x：

Urllib库
Urllin2库
Py3.x：

Urllib库
变化：

在Pytho2.x中使用import urllib2——-对应的，在Python3.x中会使用import urllib.request，urllib.error。
在Pytho2.x中使用import urllib——-对应的，在Python3.x中会使用import urllib.request，urllib.error，urllib.parse。
在Pytho2.x中使用import urlparse——-对应的，在Python3.x中会使用import urllib.parse。
在Pytho2.x中使用import urlopen——-对应的，在Python3.x中会使用import urllib.request.urlopen。
在Pytho2.x中使用import urlencode——-对应的，在Python3.x中会使用import urllib.parse.urlencode。
在Pytho2.x中使用import urllib.quote——-对应的，在Python3.x中会使用import urllib.request.quote。
在Pytho2.x中使用cookielib.CookieJar——-对应的，在Python3.x中会使用http.CookieJar。
在Pytho2.x中使用urllib2.Request——-对应的，在Python3.x中会使用urllib.request.Request。
---------------------
作者：积微成著
来源：CSDN
原文：https://blog.csdn.net/duxu24/article/details/77414298?utm_source=copy
版权声明：本文为博主原创文章，转载请附上博文链接！
"""

# GET请求

# 导入需要的库
import urllib.request
import urllib.error #（Py2）import urllib2
#（Py2）import urllib


# 定义一个字符串变量，保存要访问的链接
url = 'http://kaoshi.edu.sina.com.cn/college/scorelist?tab=batch&wl=1&local=2&batch=&syear=2013'
url1 = "https://www.baidu.com"
# 发起请求
request = urllib.request.Request(url=url1)#(Py2)request = urllib2.Request(url=url)
# 打开连接
# 超过20秒未响应则超时
response = urllib.request.urlopen(request, timeout=20)
# 读取返回内容
result = response.read().decode("utf8")
print(result)
# POST请求
