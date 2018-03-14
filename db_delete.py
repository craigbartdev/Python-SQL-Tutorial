import pymysql

db = pymysql.connect("localhost","testuser","test123","pymysql" )

cursor = db.cursor()

#delete all 21 year olds
sql = "DELETE FROM EMPLOYEE WHERE AGE = '%d'" % (21)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()