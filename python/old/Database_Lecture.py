# Database
# Connect With mySQL Database

# table, CRUD Operations,
    #C= Create  = Insert
    #R= Read    = Select
    #U= Update  = Update
    #D= Delete  =Delete

# Transcations
   # ACID=> Atomicity, Consistency, isolation, duarability
    # Commit
    # Rollback

# Errors
# DatabaseError #
    ## DataError. #  division by zero
    #InternalError. # Internal error in MySQL database
    #IntegrityError.
    #OperationalError.
    #NotSupportedError.
    #ProgrammingError.

# InterFaceError #connection fails

# Connect With MySQL Database
import pymysql
db=pymysql.connect("127.0.0.1","root","XXXXXXX","student")

# connection statement
try:
    cur=db.cursor()
    print("Connected {}".format(cur))
except ConnectionAbortedError as conerror:
    print(conerror)

# DDL (DATA DEFINITION LANGUAGE)
## CREATE,ALTER AND DROP
# DML (DATA MANIPULATION LANGUAGE)
## SELECT, INSERT, UPDATE, DELETE
# DTL (DATA TRANSCATION LANGUAGE)
## COMMIT, ROLLBACK
# DCL  (DATA CONTROL LANAGUAGE)
## ,GRANT, REVOKE

# Create Database
'''cur.execute('CREATE DATABASE student')
cur.close()'''

# Create Table
'''sql="""
    create table studentHistory(
    firstname char(200),
    lastname char(200),
    age int,
    address char(200)
    ) 
    """
cur.execute(sql)
cur.close()'''

# Another table
'''sql="""
    create table studentlog(
    firstname char(200),
    marks char(20)
    ) 
    """
cur.execute(sql)
cur.close()'''

# Insert records
#SYNATX:
#insert into <tablename>(allcolums) values(allvalues given by user)
# Insert records with 2 columns
'''sql="""
    INSERT INTO studentHistory(firstname,lastname)
    VAlUES('AJAI','BANSAL')
    """
cur.execute(sql)
db.commit()
cur.close()'''

# Insert with 4 Columns
'''sql="""
    INSERT INTO studentHistory(age,address)
    VAlUES(55,'NERUL EAST')
    """
cur.execute(sql)
db.commit()
cur.close()'''

# update records
'''sql="""
    UPDATE studentHistory 
    SET AGE=60, ADDRESS='NERUL' WHERE  firstname='AJAI'
    """
cur.execute(sql)
db.commit()
cur.close()'''

# DELETE RECORDS
'''sql="DELETE FROM studentHistory WHERE  firstname is null"
cur.execute(sql)
db.commit()
cur.close()'''


#import csv
#f=open("std.csv")


# Insert
'''sql="insert into Emp(name,age) values('Ajai',50)"
cursor1.execute(sql)
for row in csv.reader(f):
    print(row[0])
    print(row[1])
con.commit()
cursor1.close()'''

# Update
'''sql="insert into Emp(name,age) values('Ajai',50)"
cursor1.execute(sql)
con.commit()
cursor1.close()'''

# Transcation commit and rollback
'''try:
    sql="""
        INSERT INTO studentHistory(age,address)
        VAlUES(65,'vashi')
        """
    sql1="""
        INSERT INTO studentlog(firstname,marks)
        VAlUES('Jomesh','90%')
        """
    cur.execute(sql)
    cur.execute(sql1)
    db.commit()
    cur.close()
    #print('Insert Records Both tables')
except:
    db.rollback()
    print("rollback both tables records")'''

# read operations
# fetchone
# Fetchall
# rowcount
# fetchmany

# fetchall
'''sql=""" select * from studentHistory
    """
cur.execute(sql)
results=cur.fetchall()
for row in results:
    print(row[0],row[1],row[2],row[3])
cur.close()'''
# fecthone
'''sql=""" select * from studentHistory
    """
cur.execute(sql)
result=cur.fetchone()
print(result)
cur.close()'''

# rowcout
'''sql=""" select * from studentHistory
    """
cur.execute(sql)
result=cur.rowcount
print(result)
cur.close()'''

# Fetchmany
'''sql=""" select * from studentHistory
    """
cur.execute(sql)
result=cur.fetchmany(2)
print(result)
cur.close()'''

# Errors
# InterfaceErrors
'''try:
    cur=db.cursor()
    print("Connected {}".format(cur))
except ConnectionError as conerror:
    print(conerror.strerror)'''

# Database errors

try:
    sql = """ select * from studentHistory where age='AJAI'
        """
    cur.execute(sql)
    result = cur.fetchmany(2)
    print(result)
    cur.close()
except Exception as ex:
    print(ex)




