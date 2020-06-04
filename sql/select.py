import pymysql

def chaxun(sql):
    """
        查询数据mysql数据库
    """
    # pymysql 连接数据库
    db = pymysql.connect(host="127.0.0.1", user="root", password="123456", db="lipengtao")
    # 获取游标 ： 查询窗口
    cur = db.cursor()     
    # 执行sql语句
    cur.execute(sql) 
    # 得到执行的结果
    res = cur.fetchall()
    db.close()

    return res

sql = "select * from student where sno = 3"
a = chaxun(sql)
print(a)