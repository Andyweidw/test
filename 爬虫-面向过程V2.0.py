#导入类
import requests
from lxml import etree

#设置3个方法
#获取页面信息，直接调用URL参数进行配置
def get_page(url):
#输入URL
    #发送请求
    response=requests.get(url)
    #print(response)
    #获取网站编码格式

    code=response.apparent_encoding
    #print(code)
    #设置网站编码格式
    response.encoding='gbk'
    #获取页面对象
    #print(response.text)
    return response.text

#提取页面元素
def get_element(content):
    #d定义一个空列表存储元素内容
    # listen=[]
    #改成字符串拼接，设置一个空字符串
    tmp=""
    # 将页面转化成dom格式
    doc = etree.HTML(content)
    #循环提取页面上的元素
    for i in range(1,11):
        #进行元素定位
        ele = doc.xpath('/html/body/div[6]/div[1]/div['+str(i)+']/p/text()')[0]
        # 打印元素
        # print(i,ele)
        # listen.append(str(i)+ele+"\n")
        #去除掉空格
        ele = ''.join(ele.split())
        tmp=tmp+str(i)+ele+"\n"+"\n"
    print(tmp)
    return tmp

#保存页面元素
def save_page(listencot):
    # 创建文件
    file = open('文件.txt', 'a')
    # 写入内容
    file.write(str(listencot) + '\n')
    # 保存关闭文件
    file.close()

if __name__ == '__main__':
    for i in range(1,3):
        #如果是首页
        if i==1:
            url="http://www.51testing.com/html/90/category-catid-90.html"
        else:
            url = "http://www.51testing.com/html/90/category-catid-90-page-"+str(i)+".html"
        #打印页码
        print("第",i,"页")
        content=get_page(url)
        listc=get_element(content)
        save_page(listc)
