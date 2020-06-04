import pymysql

def chaxun(sql):
    """
        查询数据mysql数据库:只能select，不要delete update insert
    """
    # pymysql 连接数据库
    # host="192.144.148.91":数据库的ip地址 user="ljtest"：数据库登录账号, password="123456"：密码, db="ljtestdb"：数据库名字
    db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
    # 获取游标 ：查询窗口
    cur = db.cursor()     
    # 执行sql语句
    cur.execute(sql) 
    # 得到执行的结果
    res = cur.fetchall()
    db.close()

    return res

# sql = "select * from t_user where id = 23123123123"
# a = chaxun(sql)
# print(a)



def commit(sql):
    """
        增加/删除/修改方法：delete update insert：不要传select
    """
    # 打开数据库
    db = pymysql.connect(host="192.144.148.91", user="ljtest", password="123456", db="ljtestdb")
    # 获取游标 ： 查询窗口
    cur = db.cursor()     
    # 执行sql语句
    cur.execute(sql) 
    # 提交修改 
    db.commit()
    db.close()
    return True

# update
# sql = "update t_user set username='mcc1234' where id=254"

# insert
# sql = 'INSERT into t_admin values(NULL, "testadmin1", "admin123", NULL, NULL, "管理员2", "好好学习啊", "headimg.jpg", NULL, "女", 0, NULL, NULL, NULL)'

# delete
sql = "delete from t_admin where id=557"
commit(sql)

