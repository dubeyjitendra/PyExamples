# ##############  Flask Redirect and Errors #####################

# Flask class provides the redirect() function which redirects the user to some specified URL with the specified status code.

## An HTTP status code is a response from the server to the request of the browser. When we visit a website,
# a request is sent to the server, and the server then responds to the browser's request with a three-digit code: the HTTP status code. This status code also represents the error.

## The syntax to use the redirect() function is given below.

# syntax

# Flask.redirect(<location>,<status-code>, <response> )  

# It accepts the following parameters.

#SN	Parameter	Description
#1	location	It is the URL where the response will be redirected.
#2	status code	It is the status code that is sent to the browser's header along with the response from the server.
#3	response	It is the instance of the response that is used in the project for future requirements.


# Example

# login.py

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def home ():  
    return render_template("home.html")  
 
@app.route('/login')  
def login():  
    return render_template("login.html");  
 
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST' and request.form['pass'] == 'jtp':  
        return redirect(url_for("success"))  
    return redirect(url_for("login"))  
 
@app.route('/success')  
def success():  
    return "logged in successfully"  
  
if __name__ == '__main__':  
    app.run(debug = True)  
    
    
    
# home.html
<html>  
<head>  
<title>home</title>  
</head>  
<body>  
<h3>Welcome to the website</h3>  
<a href = "/login">login</a><br>  
</html>  

# login.html

<html>  
<head>  
    <title>login</title>  
</head>  
<body>  
    <form method = "post" action = "http://localhost:5000/validate">  
        <table>  
            <tr><td>Email</td><td><input type = 'email' name = 'email'></td></tr>  
            <tr><td>Password</td><td><input type = 'password' name = 'pass'></td></tr>  
            <tr><td><input type = "submit" value = "Submit"></td></tr>  
        </table>  
    </form>  
</body>  
</html>  



### Standard HTTP Codes
# The following HTTP codes are standardized.

#HTTP_300_MULTIPLE_CHOICES
#HTTP_301_MOVED_PERMANENTLY
#HTTP_302_FOUND
#HTTP_303_SEE_OTHER
#HTTP_304_NOT_MODIFIED
#HTTP_305_USE_PROXY
#HTTP_306_RESERVED
#HTTP_307_TEMPORARY_REDIRECT





## The abort() function

# The abort() function is used to handle the cases where the errors are involved in the requests from the client side, such as bad requests,
# unauthorized access and many more. However, the error code is to be mentioned due to which the error occurred.

### The syntax to use the abort() function is given below.
# Flask.abort(code)  


### We can mention the following error codes depending upon the specified errors.

#400: for bad requests
#401: for unauthorized access
#403: for forbidden
#404: for not found
#406: for not acceptable
#415: for unsupported media types
#429: for too many requests

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def home ():  
    return render_template("home.html")  
 
@app.route('/login')  
def login():  
    return render_template("login.html");  
 
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST' and request.form['pass'] == 'jtp':  
        return redirect(url_for("success"))  
    else:  
        abort(401)  
 
@app.route('/success')  
def success():  
    return "logged in successfully"  
  
if __name__ == '__main__':  
    app.run(debug = True)  
    
    
## Example

