#定义一个类
class spider_51():
    #定义属性
    def _init_(self):
        self.url = "http://www.51testing.com/html/90/category-catid-90.html"
    #抓取爬虫页面
    def spider_lel(self):
        file = open('文件.txt', 'w')
        response = requests.get(self.url)
        # print(response)
        # 获取网站编码格式
        code = response.apparent_encoding
        # print(code)
        # 设置网站编码格式
        response.encoding = 'gbk'
        content = response.text
        # print(response.text)
        # 将页面转化成dom格式
        self.doc = etree.HTML(content)
    #抓取元素保存大文件
    def save(self):
        for j in range(2, 4):
            for i in range(1, 11):
                ele = doc.xpath('/html/body/div[6]/div[1]/div[' + str(i) + ']/p/text()')[0]
        print(ele)
        ss = ''.join(ele.split())
        # 写入内容
        file.write(ss + '\n')

        # 发送请求
        response = requests.get('http://www.51testing.com/html/90/category-catid-90-page-2.html')
        # print(response)
        # 获取网站编码格式
        code = response.apparent_encoding
        # print(code)
        # 设置网站编码格式
        response.encoding = 'gbk'
        content = response.text
        # 将页面转化成dom格式
        doc = etree.HTML(content)

    # 保存关闭文件
    file.close()
    #实例化兑现

    #调用类的方法