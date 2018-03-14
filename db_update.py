import pymysql

# Open database connection
db = pymysql.connect("localhost","testuser","test123","pymysql" )

# prepare a cursor object 
cursor = db.cursor()

# add one year to the age of all males
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
            WHERE SEX = '%c'" % ('M')

try:
   cursor.execute(sql)
   
   db.commit()
except:

   db.rollback()

# disconnect from server
db.close()