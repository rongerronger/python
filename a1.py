r1={"name":"王蓉","age":25,"salary":9000,"city":"杭州"}
r2={"name":"张三","age":30,"salary":12000,"city":"西安"}
r3={"name":"李四","age":28,"salary":10000,"city":"杭州"}
tb=[r1,r2,r3]
print(tb[1].get("salary"))

for i in range(len(tb)):
    print(tb[i].get("salary"))

for i in range(len(tb)):
    print(tb[i].get("name"),tb[i].get("age"),tb[i].get("salary"),tb[i].get("city"))
    
