#定义3个方法
#def calc_GUI()
#def calc_data()
#def calc_result()


#画界面
def calc_GUI():
    print("******************************************")
    print("*          1、计算器加法                   *")
    print("*          2、计算器减法                   *")
    print("*          3、计算器乘法                   *")
    print("*          4、计算器除法                   *")
    print("******************************************")


#进行计算
def calc_data():
    x = int(input("请输入数字"))
    y = int(input("请输入数字"))

    # 输入运算符号
    z = int(input('请输入编号：'))




#输出结果
def calc_result():
# 判断运算符号
    if (z == 1):
        jieguo = x + y
    elif (z == 2):
        jieguo = x - y
    elif (z == 3):
        jieguo = x * y
    elif (z == 4):
        jieguo = x / y
    else:
        print("输入运算符错误")
    print(jieguo)



#调用函数
if __name__ == '__main__':
    calc_GUI()
    calc_data()
    calc_result()

