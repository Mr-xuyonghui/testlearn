import pprint

import pymysql
from seleniumlearn.BasePages.BasePage import SqlHandler
#连接数据库，需要看下connect是如何入参的
# db =pymysql.connect(host="10.100.130.84",user='root',password='root',database='activity',charset='utf8')
# #创建游标
# cursor=db.cursor()
# #cursor.execute("SELECT VERSION()")
# cursor.execute("update `activity`.`activity_confession_wall` set style_ids = %s where id = 1"
#               ,('[{"style_id":3,"position":1},{"style_id":1,"position":2},{"style_id":2,"position":3},{"style_id":4,"position":4},{"style_id":5,"position":5}]',))
# #进行更新，删除等操作需要提交，不然无法保存新建或者修改的数据
# db.commit()
# #执行sql语句
# effect_row=cursor.execute("SELECT * FROM `activity`.`activity_confession_wall` LIMIT 0,1000")
# #获取sql结果的第一条
# data= cursor.fetchone()
# print("sql语句影响行数:",effect_row)
# print("type is {},value = {}".format(type(data),data))
# print(cursor.lastrowid)
# #关闭游标，可以使用with 语句简化连接或者创建游标
# cursor.close()
# #关闭数据库连接
# db.close()


"""
通过封装的sql函数进行数据库操作
"""
db = SqlHandler("10.100.130.84",'root','root','activity')
search_sql="SELECT * FROM `activity`.`activity_confession_wall`"
update_sql="update `activity`.`activity_confession_wall` set style_ids = %s where id = 1"
updata_pram='[{"style_id":3,"position":1},{"style_id":1,"position":2},{"style_id":2,"position":3},{"style_id":4,"position":4}]'
res= db.get_inti_size(1,search_sql)
pprint.pprint(res)
upres=db.update_data(update_sql,updata_pram)
res_1=db.get_one(search_sql)
pprint.pprint(res_1)