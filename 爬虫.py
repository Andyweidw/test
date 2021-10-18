#导入类库包
import requests
from lxml import etree
#初始化URL
url="http://www.51testing.com/html/90/category-catid-90.html"

#发送请求
response=requests.get(url)
#print(response)
#获取网站编码格式
code=response.apparent_encoding
#print(code)
#设置网站编码格式
response.encoding='gbk'
content=response.text
#print(response.text)
#将页面转化成dom格式
doc=etree.HTML(content)
#抓取元素
for i in range(1,11):
    ele=doc.xpath('/html/body/div[6]/div[1]/div['+str(i)+']/p/text()')[0]
#打印元素
    print(ele)
    print("\n")



