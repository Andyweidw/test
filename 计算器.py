#绘制界面
print("******************************************")
print("*          1、计算器加法                   *")
print("*          2、计算器减法                   *")
print("*          3、计算器乘法                   *")
print("*          4、计算器除法                   *")
print("******************************************")
#输入2个数字
x=int(input("请输入数字"))
y=int(input("请输入数字"))

#输入运算符号
z=int(input('请输入编号：'))
#判断运算符号
if(z==1):
    jieguo=x+y
elif(z==2):
    jieguo=x-y
elif(z==3):
    jieguo=x*y
elif(z==4):
    jieguo=x/y
else:
    print("输入运算符错误")
#得出结果
print(jieguo)