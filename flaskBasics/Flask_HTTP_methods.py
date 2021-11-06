#############  Flask HTTP methods  ##################

# The methods are given in the following table.

#1	GET	    It is the most common method which can be used to send data in the unencrypted form to the server.
#2	HEAD	It is similar to the GET but used without the response body.
#3	POST	It is used to send the form data to the server. The server does not cache the data transmitted using the post method.
#4	PUT	    It is used to replace all the current representation of the target resource with the uploaded content.
#5	DELETE	It is used to delete all the current representation of the target resource specified in the URL.


## POST Method

#### login.html

<html>  
   <body>  
      <form action = "http://localhost:5000/login" method = "post">  
         <table>  
        <tr><td>Name</td>  
        <td><input type ="text" name ="uname"></td></tr>  
        <tr><td>Password</td>  
        <td><input type ="password" name ="pass"></td></tr>  
        <tr><td><input type = "submit"></td></tr>  
    </table>  
      </form>  
   </body>  
</html>  

## post_example.py

from flask import *  
app = Flask(__name__)  
  
@app.route('/login',methods = ['POST'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="jitendra" and passwrd=="google":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  
   
   
   
   
   
#### GET Method

# login.html

<html>  
   <body>  
      <form action = "http://localhost:5000/login" method = "get">  
         <table>  
        <tr><td>Name</td>  
        <td><input type ="text" name ="uname"></td></tr>  
        <tr><td>Password</td>  
        <td><input type ="password" name ="pass"></td></tr>  
        <tr><td><input type = "submit"></td></tr>  
    </table>  
      </form>  
   </body>  
</html>  


## get_example.py

from flask import *  
app = Flask(__name__)  
  
  
@app.route('/login',methods = ['GET'])  
def login():  
      uname=request.args.get('uname')  
      passwrd=request.args.get('pass')  
      if uname=="jitendra" and passwrd=="google":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  
   
   
### The data is obtained by using the following line of code.

####  uname = request.args.get('uname')  

####  Here, the args is a dictionary object which contains the list of pairs of form parameter and its corresponding value.

#### This is an important difference between the GET requests and the 
#### POST requests as the data sent to the server is not shown in the URL on the browser in the POST requests.

   