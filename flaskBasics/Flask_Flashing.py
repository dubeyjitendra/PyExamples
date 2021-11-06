########  Flask Flashing #######################

## In the web applications, there are scenarios where the developer might need to flash the messages to provide feedback to the users for the behavior of the application
# in different cases.

# Flask provides the flash() method, in the same way, the client-side scripting language like JavaScript uses the alerts or the python GUI 
#framework Tkinter uses the dialogue box or the message box.

#The flash() method is used to generate informative messages in the flask. It creates a message in one view and renders it to a template view function called next.


# 
## In the web applications, there are scenarios where the developer might need to flash the messages to provide feedback to the users for the behavior of the application in different cases.

##Flask provides the flash() method, in the same way, the client-side scripting language like JavaScript uses the alerts or the python GUI framework Tkinter uses the dialogue box or the message box.

##The flash() method is used to generate informative messages in the flask. It creates a message in one view and renders it to a template view function called next.


 #In other# words, the flash() method of the flask module passes the message to the next request which is an HTML template. The syntax to use the flash() method is given below.
 
 # syntax
 
 # flash(message, category) 
 
 
 
 # It accepts the following parameters.

#message: it is the message to be flashed to the user.
#Category: It is an optional parameter. Which may represent any error, information, or warning.


## The messages are generated in the flask script using the flash() method of flask module. 
#These messages need to be extracted in the template from the session. For this purpose, the method get_flashed_messages() is called in the HTML template.

#The syntax to use this method is given below.

# get_flashed_messages(with_categories, category_filter)    

# It accepts the following parameters.

#with_categories: This parameter is optional and used if the messages have the category.
#category_filter: This parameter is also optional. It is useful to display only the specified messages.


# Example

# The example contains the flask and HTML scripts for server and client-side scripting.

#The python script flashes the messages and redirects the user to the different HTML script depending upon the successful and unsuccessful login of the user.

###  flashing.py

from flask import *  
app = Flask(__name__)  
app.secret_key = "abc"  
 
@app.route('/index')  
def home():  
    return render_template("index.html")  
 
@app.route('/login',methods = ["GET","POST"])  
def login():  
    error = None;  
    if request.method == "POST":  
        if request.form['pass'] != 'jtp':  
            error = "invalid password"  
        else:  
            flash("you are successfuly logged in")  
            return redirect(url_for('home'))  
    return render_template('login.html',error=error)  
  
      
if __name__ == '__main__':  
    app.run(debug = True) 
    
    
    
# index.html

<html>  
<head>  
<title>home</title>  
</head>  
<body>  
    {% with messages = get_flashed_messages() %}  
         {% if messages %}  
               {% for message in messages %}  
                    <p>{{ message }}</p>  
               {% endfor %}  
         {% endif %}  
      {% endwith %}  
<h3>Welcome to the website</h3>  
<a href = "{{ url_for('login') }}">login</a>  
</body>  
</html>  


# login.html
<html>  
<head>  
    <title>login</title>  
</head>  
<body>  
    {% if error %}  
        <p><strong>Error</strong>: {{error}}</p>  
    {% endif %}  
  
    <form method = "post" action = "/login">  
        <table>  
            <tr><td>Email</td><td><input type = 'email' name = 'email'></td></tr>  
            <tr><td>Password</td><td><input type = 'password' name = 'pass'></td></tr>  
            <tr><td><input type = "submit" value = "Submit"></td></tr>  
        </table>  
    </form>  
</body>  
</html>



