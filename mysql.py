import mysql.connector
cnx=mysql.connector.connect(user='root',password='root',database='K')
cursor=cnx.cursor()
qurey="swlect * from Persons"
results=cursor.fetchall()
for result in results:
    print(result)