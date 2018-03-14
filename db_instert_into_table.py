import pymysql

#open db connection 
db = pymysql.connect("localhost", "testuser", "test123", "pymysql")

#prepare cursor
cursor = db.cursor()

#prepare sql query to statically INSERT a record into db
'''
sql = """INSERT INTO EMPLOYEE
            (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
        VALUES 
            ('Mac', 'Mohan', 20, 'M', 2000)""" '''
#prepare sql query to dynamically INSERT a record into db
sql = "INSERT INTO EMPLOYEE\
            (FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) \
        VALUES \
            ('%s', '%s', '%d', '%c', '%d')" % \
            ('Tim', 'Johnson', 21, 'M', 4500)
             #string, string, digit, char, digit
             #alternatively can set data as variables and pass those in as well

try:
    #execute sql command
    cursor.execute(sql)
    #commit changes in db
    db.commit()
except:
    #rollback to previous state if there is an error
    db.rollback()

#disconnect from server
db.close()