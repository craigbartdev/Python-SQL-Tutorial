import pymysql

#open db. hostname, username, password, dbname
db = pymysql.connect("localhost", "testuser", "test123", "pymysql")

#prepare cursor
cursor = db.cursor()

#execute SQL query using execute() method
cursor.execute("SELECT VERSION()")

#fetch single row with fetchone method
data = cursor.fetchone()

print("Database version: %s " % data)

#disconnect from server
db.close()
