############################### Flask Session #######################


## The concept of a session is very much similar to that of a cookie. However, the session data is stored on the server.

## The session can be defined as the duration for which a user logs into the server and logs out.
##  The data which is used to track this session is stored into the temporary directory on the server.

## The session data is stored on the top of cookies and signed by the server cryptographically.


## In the flask, a session object is used to track the session data which is a dictionary object that contains a key-value pair
## of the session variables and their associated values.

## The following syntax is used to set the session variable to a specific value on the server.

# Session[<variable-name>] = <value>  


## To remove a session variable, use the pop() method on the session object and mention the variable to be removed.

#session.pop(<variable-name>, none)  

## Example

from flask import *  
app = Flask(__name__)  
app.secret_key = "abc"  
 
@app.route('/')  
def home():  
    res = make_response("<h4>session variable is set, <a href='/get'>Get Variable</a></h4>")  
    session['response']='session#1'  
    return res;  
 
@app.route('/get')  
def getVariable():  
    if 'response' in session:  
        s = session['response'];  
        return render_template('getsession.html',name = s)  
  
if __name__ == '__main__':  
    app.run(debug = True)  
    
    
## getsession.html

<html>  
<head>  
<title>getting the session</title>  
</head>  
<body>  
<p>The session is set with value: <strong>{{name}}</strong></p>  
</body>  
</html>  




# Now, the user has to login again with the email and password to view the profile on the application.

# This is a simple login application built using python flask that implements the session.
# Here, the flask script login.py acts like the main controller which contains the view functions (home(), login(), success(), logout(), and profile()) 
# which are associated with the URL mappings (/, /login, /success, /logout, /profile) respectively.


# login.py

from flask import *  
app = Flask(__name__)  
app.secret_key = "ayush"  
 
@app.route('/')  
def home():  
    return render_template("home.html")  
 
@app.route('/login')  
def login():  
    return render_template("login.html")  
 
@app.route('/success',methods = ["POST"])  
def success():  
    if request.method == "POST":  
        session['email']=request.form['email']  
    return render_template('success.html')  
 
@app.route('/logout')  
def logout():  
    if 'email' in session:  
        session.pop('email',None)  
        return render_template('logout.html');  
    else:  
        return '<p>user already logged out</p>'  
 
@app.route('/profile')  
def profile():  
    if 'email' in session:  
        email = session['email']  
        return              render_template('profile.html',name=email)  
    else:  
        return '<p>Please login first</p>'  
  
if __name__ == '__main__':  
    app.run(debug = True)  
    
    
## home.html

<html>  
<head>  
<title>home</title>  
</head>  
<body>  
<h3>Welcome to the website</h3>  
<a href = "/login">login</a><br>  
<a href = "/profile">view profile</a><br>  
<a href = "/logout">Log out</a><br>  
</body>  
</html>  


## login.html

<html>  
<head>  
    <title>login</title>  
</head>  
<body>  
    <form method = "post" action = "http://localhost:5000/success">  
        <table>  
            <tr><td>Email</td><td><input type = 'email' name = 'email'></td></tr>  
            <tr><td>Password</td><td><input type = 'password' name = 'pass'></td></tr>  
            <tr><td><input type = "submit" value = "Submit"></td></tr>  
        </table>  
    </form>  
</body>  
</html>


## success.html

<html>  
<head>  
<title>success</title>  
</head>  
<body>  
    <h2>Login successful</h2>  
    <a href="/profile">View Profile</a>  
</body>  
</html> 

## logout.html

<html>  
<head>  
    <title>logout</title>  
</head>  
  
<body>  
<p>logout successful, click <a href="/login">here</a> to login again</p>  
</body>  
  
</html> 