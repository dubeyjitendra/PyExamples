##########################  Flask SQLite   ####################################

# CRUD Application in flask

## EmoloyeeDB.py

import sqlite3  
  
con = sqlite3.connect("employee.db")  
print("Database opened successfully")  
  
con.execute("create table Employees (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE NOT NULL, address TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()  


@app.route("/")  
def index():  
    return render_template("index.html");  
    
@app.route("/savedetails",methods = ["POST","GET"])  
def saveDetails():  
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"]  
            address = request.form["address"]  
            with sqlite3.connect("employee.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Employees (name, email, address) values (?,?,?)",(name,email,address))  
                con.commit()  
                msg = "Employee successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
        finally:  
            return render_template("success.html",msg = msg)  
            con.close() 

            
@app.route("/deleterecord",methods = ["POST"])  
def deleterecord():  
    id = request.form["id"]  
    with sqlite3.connect("employee.db") as con:  
        try:  
            cur = con.cursor()  
            cur.execute("delete from Employees where id = ?",id)  
            msg = "record successfully deleted"  
        except:  
            msg = "can't be deleted"  
        finally:  
            return render_template("delete_record.html",msg = msg)  
            
app.route("/view")  
def view():  
    con = sqlite3.connect("employee.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from Employees")  
    rows = cur.fetchall()  
    return render_template("view.html",rows = rows)   
            
## index.html

<!DOCTYPE html>  
<html>  
<head>  
    <title>home</title>  
</head>  
<body>  
    <h2>Hi, welcome to the website</h2>  
    <a href="/add">Add Employee</a><br><br>  
    <a href ="/view">List Records</a><br><br>  
    <a href="/delete">Delete Record</a><br><br>  
</body>  
</html>



## add.html

<!DOCTYPE html>  
<html>  
<head>  
    <title>Add Employee</title>  
</head>  
<body>  
    <h2>Employee Information</h2>   
    <form action = "/savedetails" method="post">  
    <table>  
        <tr><td>Name</td><td><input type="text" name="name"></td></tr>  
        <tr><td>Email</td><td><input type="email" name="email"></td></tr>  
        <tr><td>Address</td><td><input type="text" name="address"></td></tr>  
        <tr><td><input type="submit" value="Submit"></td></tr>  
    </table>  
    </form>  
</body>  
</html>  

## success.html
<!DOCTYPE html>  
<html>  
<head>  
    <title>save details</title>  
</head>  
<body>  
    <h3>Hi Admin, {{msg}}</h3>  
    <a href="/view">View Employees</a>  
</body>  
</html>  

## delete.html
<!DOCTYPE html>  
<html>  
<head>  
    <title>delete record</title>  
</head>  
<body>  
  
    <h3>Remove Employee from the list</h3>  
  
<form action="/deleterecord" method="post">  
Employee Id <input type="text" name="id">  
<input type="submit" value="Submit">  
</form>  
</body>  
</html>


## delete_record.html
<!DOCTYPE html>  
<html>  
<head>  
    <title>delete record</title>  
</head>  
<body>  
<h3>{{msg}}</h3>  
<a href="/view">View List</a>  
</body>  
</html>  


## view.html
<!DOCTYPE html>  
<html>  
<head>  
    <title>List</title>  
</head>  
<body>  
  
<h3>Employee Information</h3>  
<table border=5>  
    <thead>  
        <td>ID</td>  
        <td>Name</td>  
        <td>Email</td>  
        <td>Address</td>  
    </thead>  
      
    {% for row in rows %}  
      
        <tr>  
            <td>{{row["id"]}}</td>  
            <td>{{row["name"]}}</td>  
            <td>{{row["email"]}}</td>  
            <td>{{row["address"]}}</td>  
        </tr>  
      
    {% endfor %}  
</table>  
<br><br>  
  
<a href="/">Go back to home page</a>  
  
</body>  
</html>  

## crud.py

