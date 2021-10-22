import requests
from lxml import etree

#定义一个URL
url="https://baijiahao.baidu.com/s?id=1714010128306417698"
#获取页面返回数据
response=requests.get(url)
code=response.apparent_encoding
response.encoding='utf-8'
#转换成doc格式
content=response.text
doc=etree.HTML(content)
# #抓取元素
ele=doc.xpath('//*[@id="ssr-content"]/div[2]/div[2]/div[1]/div[1]/div[2]/p/span/text()')[0]
print(ele)

