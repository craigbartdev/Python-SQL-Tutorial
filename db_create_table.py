import pymysql

#open db connection
db = pymysql.connect("localhost", "testuser", "test123", "pymysql")

#prepare cursor
cursor = db.cursor()

#drop table if it already exists using exeecute() method
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")  #overwrite table if exists

#create table as per requirement
sql = """CREATE TABLE EMPLOYEE ( 
    FIRST_NAME CHAR(20) NOT NULL,
    LAST_NAME CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT )"""

cursor.execute(sql)

#disconnect from server
db.close()

