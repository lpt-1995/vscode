# a = [1,2,3,4]   #遍历列表
# for i in a:     #for循环中的in是赋值
#     print(i)

# d = {"username":"哈哈","password":"789"}
# for i in d:
#     #print(i)    遍历key
#     #print(d[i])  遍历value  如果不存在 则报错
#     print(d.get(i))   #遍历value  get不会报错 

# db = [
#        {"username":"张三","password":"264"},
#        {"username":"李四","password":"435"}
#     ]

# zh = input("请输入账号：")
# mm = input("请输入密码：")

# for i in db:
#     if zh == i.get("username"):
#         if mm == i.get("password"):
#            print("输入的账号{}登录成功！".format(zh))
#            break 
#     else:
#         print("登录失败！")  

# sum = 0
# x = 1
# while True:
#     sum = sum + x
#     x = x+1
#     if x > 100:
#         break   #满足条件直接退出循环
# print(sum)

#作业：输入密码

# db = [{"username":'李连杰','password':'234'},
#       {"username":"张三","password":"264"},
#       {"username":"李四","password":"435"}
#       ]
# count = 1
# u = input("请输入账号：")         
# p = input("请输入密码：")

# for i in db:   # i是db的元素，即字典
#     if u == i.get("username"):
#        i["password"] = p      #可以需改
#        break   
#     else:
#         if len(db) == count:
#            db.append({"username":u,'password':p})
#     #    c = {}
#     #    c["username"] = u
#     #    c["password"] = p    
#     #    db.append(c)   
#     count = count + 1       
# print(db)
# print(count)

# def sum(g, h):   #方法  
#     he = g + h
#     return he 

# a = 1
# b = 2

# s1 = sum(a, b)

# print(s1)

import pymysql

def chaxun(sql):
    """
        查询数据mysql数据库
    """
    # pymysql 连接数据库
    db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="lipengtao")
    # 获取游标 （查询窗口）
    cur = db.cursor()     
    # 执行sql语句
    cur.execute(sql) 
    # 得到执行的结果
    res = cur.fetchall()
    db.close()

    return res

sql = "select * from student where sno = 2"
a = chaxun(sql)
print(a)

     
      