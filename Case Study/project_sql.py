import mysql.connector

conn = mysql.connector.connect(
         user='root',
         password='$agar@hire12',
         host='localhost',
         database='project1'
        )

mycursor = conn.cursor()
mycursor.execute("Show databases")

print("The databases in MySql are:")
for i in mycursor:
    print(i)

mycursor.execute("Select * from project_table")

result = mycursor.fetchall()
print("The Student Information is:")
for i in result:
    print(i)

a = int(input("Enter Prn no."))
b = input("Enter first name")
c = input("Enter middle name")
d = input("Enter last name")
e = input("Enter Address")
f = input("Enter Moblie number")
g = input("Enter Email Id")
h = input("Enter Date of birth")

s = 'INSERT INTO project_table VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
t = (a,b,c,d,e,f,g,h)
mycursor.execute(s,t)
conn.commit()

mycursor.execute("Select * from project_table")
result = mycursor.fetchall()
print("The Student Information is:")
for i in result:
    print(i)

prn_no= int(input("Enter the prn number you want to delete")) 
rm = "DELETE from project_table WHERE prn_no=%s"
val1 = (prn_no,)
mycursor.execute(rm,val1)
conn.commit()

mycursor.execute("Select * from project_table")
result = mycursor.fetchall()
print("The Student Information is:")
for i in result:
    print(i)

p = input("Enter existing address")
q = input("Enter new address")
ch = "UPDATE project_table SET address=%s WHERE Address=%s"
val3 = (q,p)
mycursor.execute(ch,val3)
conn.commit()

mycursor.execute("Select * from project_table")
result = mycursor.fetchall()
print("The Student Information is:")
for i in result:
    print(i)

col = "ALTER TABLE student_table ADD CGPA VARCHAR(100) AFTER dob"
prnNo = input("Enter your Prn number")
CGPA = input("Enter CGPA")
cgpaUp = "UPDATE student_table SET CGPA=%s where prn_no=%s"
val4 = (CGPA,)
mycursor(cgpaUp,val4)
mycursor.execute(col)

mycursor.execute("Select * from project_table")
result = mycursor.fetchall()
print("The Student Information is:")
for i in result:
    print(i)

conn.close()
