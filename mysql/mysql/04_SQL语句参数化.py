'''SQL语句参数化'''
import pymysql

db = pymysql.connect(host="localhost",user="root",
                     password="123456",
                     database="db5",
                     charset="utf8")
cursor = db.cursor()

while True:
    c = input("按q退出,按回车输入学生信息:")
    if c.strip().lower() == "q":
        break

    name = input("请输入姓名:")
    score = input("请输入成绩:")

    try:
        ins = "insert into t1(name,score) values(%s,%s)"
        # 此方法不推荐使用
        # ins = "insert into t1(name,score) values('%s','%s')" % (name,socre)

        # execute(sql,列表)
        cursor.execute(ins,[name,score])
        db.commit()
        print("ok")
    except Exception as e:
        db.rollback()
        print("Failed",e)

cursor.close()
db.close()






