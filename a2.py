#测试选择结构的嵌套
score=int(input("请输入一个0-100之间的分数:"))
grade=""

if score>100 or score<0:
    score=int(input("输入错误"))
else:
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="E"
    print("分数为{0}，等级为{1}".format(score,grade))
    
        
#while结构
num=0
while num<10:
    print(num,end="\t")
    num+=1


#for
d={"name":"wang","age":18,"job":"测试员"}
for x in d:
    print(x)
for x in d.keys():
    print(x)
for x in d.values():
    print(x)
for x in d.items():
    print(x)

#累加和
sum_all=0
sum_odd=0
sum_even=0
for x in range(101):
    sum_all+=x
    if x%2==1:
        sum_odd+=x
    else:
        sum_even+=x
print("1-100累加总和{0}，奇数和{1}，偶数和{2}".format(sum_all,sum_odd,sum_even))


#嵌套循环

for x in range(5):
    for y in range(5):
        print(x,end="\t")
    print() #起换行的作用

#99乘法表
for m in range(10):
    for n in range(1,m+1):
        print("{0}*{1}={2}".format(m,n,(m*n)),end="\t")
    print()
    
#列表字典
r1=dict(name="ww",age=18,salary=50000)
r2=dict(name="tt",age=33,salary=1000000)
r3={"name":"硕士","age":24,"salary":400000}
tb=[r1,r2,r3]
for x in tb:
    if x.get("age")>20 and x.get("salary")>800000:
        print(x)


#循环代码优化
import time
start=time.time()
for i in range(1000):
    result=[]
    for m in range(10000):
        result.append(i*1000+m*100)
end=time.time()
print("耗时:{0}".format((end-start)))


start2=time.time()         #优化后
for i in range(1000):
    result=[]
    c=i*1000
    for m in range(10000):
        result.append(c+m*100)
end2=time.time()
print("耗时:{0}".format((end2-start2)))


#并行迭代

names=("zhan","yiyi","网")
ages=(11,22,33,44,5,5)
jobs=("老师","音乐家","程序员","ceshiyuan")
for name,age,job,in zip(names,ages,jobs):
    print("{0}---{1}---{2}".format(name,age,job))


#推导式


#绘同心圆
import turtle
t=turtle.Pen()
my_colors=("red","green","yellow","black")
t.width(4)
t.speed(10)
for i in range(66):
    t.penup()
    t.goto(0,-i*10)
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle((i+1)*10)
 
turtle.done()
