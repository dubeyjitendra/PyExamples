# DBMS
# RDBMS
# Database
# Connect With mySQL Database

# table, CRUD Operations,
    #C= Create  = Insert
    #R= Read    = Select
    #U= Update  = Update
    #D= Delete  =Delete


# Transcations
   # ACID=> Atomicity, Consistency, isolation, duarability
    # Commit =perma
    # Rollback ##

# Errors
# DatabaseError #
    ## DataError. #  division by zero
    #InternalError. # Internal error in MySQL database
    #IntegrityError.
    #OperationalError.
    #NotSupportedError.
    #ProgrammingError.


# DDL (DATA DEFINITION LANGUAGE)
## CREATE,ALTER AND DROP
# DML (DATA MANIPULATION LANGUAGE)
## SELECT, INSERT, UPDATE, DELETE
# TCL (transcation TRANSCATION LANGUAGE)
## COMMIT, ROLLBACK
# DCL  (DATA CONTROL LANAGUAGE)
## ,GRANT, REVOKE


## constraints
    ## primary key prim
    ## foreign key
    ## unique key
    ## composite key
    ## check
    ## index


## Query
    ## subquery
    ## Conditional QUery
    ## Joins
    ## procedure
    ## function
        ## user defined function
        ## built-in function
    ## trigger
    ### cursor

#joins
 ## inner join
 ## full outer join
 ### left outer join
 #### right outer join
 ###### self join


## DBA()
 ## backup/restore
 ##  Comamads
 ## profilling
 ## mirrioring
 ## data warehouing
 ## failour


import sqlite3


### connection create

# create database 'test'
class DB_operations:

    def create_connection(self):
        try:
            conn = sqlite3.connect("test.db")
            # print(sqlite3.version)
            return conn
        except Exception as e:
            print("Connection Error ==", e)


    def create_table(self):
        try:

            conn = self.create_connection() ## create a connection
            cur = conn.cursor() ## create a cursor object
            sql_statement = """
                                create table user (
                                id  INTEGER primary key autoincrement,
                                Name text,
                                create_date timestamp default CURRENT_TIMESTAMP
                                )
                                
                            """
            cur.execute(sql_statement)
        except Exception as e:
            print("while creating table getting error==",e)

        finally:
            cur.close()
            conn.close()


    def insert(self):
        try:

            conn = self.create_connection()  ## create a connection
            cur = conn.cursor()  ## create a cursor object
            name1 = 'john'
            sql_statement = """
                                insert into user (Name) values ('"""+str(name1)+"""');
                            """
            cur.execute(sql_statement)
            conn.commit()
            print("table inserted successfully")

        except Exception as e:
            print("while creating table getting error==", e)

        finally:
            cur.close()
            conn.close()


    def update(self):
        try:

            conn = self.create_connection()  ## create a connection
            cur = conn.cursor()  ## create a cursor object

            sql_statement = """
                                update user set Name="Sid-Nitesh" where Name= 'John';
                            """
            cur.execute(sql_statement)
            conn.commit()
            print("table updated successfully")

        except Exception as e:
            print("error==", e)

        finally:
            cur.close()
            conn.close()
    # create_table()

    def delete(self):
        try:

            conn = self.create_connection()  ## create a connection
            cur = conn.cursor()  ## create a cursor object
            sql_statement = """
                               delete from user where Name= 'Rushab';
                               
                               
                            """
            cur.execute(sql_statement)
            # conn.rollback()
            conn.commit()
            print("table deleted successfully")

        except Exception as e:
            print("error==", e)

        finally:
            cur.close()
            conn.close()

    def queru_result(self):
        try:

            conn = self.create_connection()  ## create a connection
            cur = conn.cursor()  ## create a cursor object
            sql_statement = """
                               select * from user;


                            """
            currall = cur.execute(sql_statement)
            for curr in currall.fetchall():
                print(curr)


        except Exception as e:
            print("error==", e)

        finally:
            cur.close()
            conn.close()

obj = DB_operations()
obj.insert()
obj.queru_result()



# if __name__=='__main__':
#     create_table()





### questions

"""
Write a Python program to create a SQLite database and connect with the database and print the version of the SQLite database
Write a Python program to create a SQLite database connection to a database that resides in the memory.
Write a Python program to connect a database and create a SQLite table within the database.
Write a Python program to insert values to a table from user input
Write a Python program to insert a list of records into a given SQLite table
Write a Python program to delete a specific row from a given SQLite table.

"""
















