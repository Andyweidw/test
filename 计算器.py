#绘制界面





#输入2个数字
x=int(input())
y=int(input())

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