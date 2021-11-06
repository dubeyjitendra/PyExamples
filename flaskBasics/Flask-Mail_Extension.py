

# How to install flask-mail extension

# pip install Flask-Mail


# 1	MAIL_SERVER	        It represents the name or IP address of the email server. The default is localhost.
# 2	MAIL_PORT	        It represents the port number of the server. Default port number is 25.
# 3	MAIL_USE_TLS	    It is used to enable or disable the transport security layer description. The default is false.
# 4	MAIL_USE_SSL	    It is used to enable or disable the secure socket layer description. The default value is false.
# 5	MAIL_DEBUG	        It is used to provide the debug support to the mail application. The default value is None.
# 6	MAIL_USERNAME	    It represents the user name of the sender. The default value is None.
# 7	MAIL_PASSWORD	    It represents the password of the server email id. The default value is None.
# 8	MAIL_DEFAULT_SENDER	It is used to set the default sender id for the multiple emails. The default value is None.
# 9	MAIL_MAX_EMAILS	    It is used to set the maximum number of email to be sent. The default value is None.
# 10 MAIL_SUPPRESS_SEND	Sending the mail is suppressed if the app.testing is set to the true.
# 11 MAIL_ASCII_ATTACHMENTS	If it is set to true, attached file names are converted to ASCII. The default is False.


# Process of sending email using flask web application

# Step 1: import the required module like flask-mail, flask using from-import statement.
from flask import *  
from flask-mail import *  

# Step 2: Configure the Flask Mail.
app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'admin@gmail.com'  
app.config['MAIL_PASSWORD'] = '******'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  

# Step 3: Instantiate the Mail class.
mail = Mail(app)  

# Step 4: Instantiate the Message class with the desired attributes in the function mapped by some URL rule.
@app.route('/')  
def index():  
    msg = Message('subject', sender = 'admin@gmail.com', recipients=['username@gmail.com'])  
    msg.body = 'hi, this is the mail sent by using the flask web application'  
    return "Mail Sent, Please check the mail id"  
    
    
    
# Example
# The following example contains a python script where we send the email to the given email id.

# Mailer.py



from flask import *  
from flask-mail import *  
  
app = Flask(__name__)  
  
#Flask mail configuration  
app.config['MAIL_SERVER']='smtp.gmail.com'  
app.config['MAIL_PORT']=465  
app.config['MAIL_USERNAME'] = 'admin@gmail.com'  
app.config['MAIL_PASSWORD'] = '******'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
#instantiate the Mail class  
mail = Mail(app)  
  
#configure the Message class object and send the mail from a URL  
@app.route('/')  
def index():  
    msg = Message('subject', sender = 'admin@gmail.com', recipients=['username@gmail.com'])  
    msg.body = 'hi, this is the mail sent by using the flask web application'  
    return "Mail Sent, Please check the mail id"  
  
if __name__ == '__main__':  
    app.run(debug = True)  







##############################
###############################

#  Email verification in flask using OTP

# In the modern web applications, sometimes the email is verified using the one time password generated randomly by the program. In this example, we will create a python script that accepts the user's email id as the input from the user and send an email containing the automatically (randomly) generated (4-digit) one-time password.
# For the successful verification of the email-id, the user is required to enter the otp sent to the mentioned email id. If the OTP entered by the user is matched with the randomly generated OTP, then the email-id is successfully verified, and the success message is shown to the user otherwise the verification is failed, and the failure message is shown to the user.
# In the below example, A flask script Mailer.py acts as a controller with the functions verify() and validate() associated with the URL /verify and /validate respectively. These functions also render the HTML templates to accept the input from the user and show the result depending upon the email verification.

# Mailer.py

from flask import *  
from flask_mail import *  
from random import *  
  
app = Flask(__name__)  
mail = Mail(app)  
  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465     
app.config["MAIL_USERNAME"] = 'username@gmail.com'  
app.config['MAIL_PASSWORD'] = '*************'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
mail = Mail(app)  
otp = randint(000000,999999)  
 
@app.route('/')  
def index():  
    return render_template("index.html")  
 
@app.route('/verify',methods = ["POST"])  
def verify():  
    email = request.form["email"]  
      
    msg = Message('OTP',sender = 'username@gmail.com', recipients = [email])  
    msg.body = str(otp)  
    mail.send(msg)  
    return render_template('verify.html')  
 
@app.route('/validate',methods=["POST"])  
def validate():  
    user_otp = request.form['otp']  
    if otp == int(user_otp):  
        return "<h3>Email verified successfully</h3>"  
    return "<h3>failure</h3>"  
  
if __name__ == '__main__':  
    app.run(debug = True) 



# index.html
<!DOCTYPE html>  
<html>  
<head>  
    <title>index</title>  
</head>  
<body>  
<form action = "http://localhost:5000/verify" method = "POST">  
Email: <input type="email" name="email">  
<input type = "submit" value="Submit">  
</form>  
</body>  
</html>  

# verify.html

<!DOCTYPE html>  
<html>  
<head>  
    <title>OTP Verification</title>  
</head>  
  
<body>  
  
<form action = "/validate" method="post">  
  
<h4> One-time password has been sent to the email id. Please check the email for the verification.</h4>  
  
Enter OTP: <input type="text" name="otp">  
  
<input type="submit" value="Submit">  
  
</form>  
</body>  
</html>




########################################
########################################

# Bulk Emails
from flask import *  
from flask_mail import *  
  
app = Flask(__name__)  
  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465  
app.config["MAIL_USERNAME"] = 'admin@gmail.com'  
app.config['MAIL_PASSWORD'] = '******'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
users = [{'name':'john','email':'john@gmail.com'},{'name':'Ayush','email':'ayush@javatpoint.com'},{'name':'david','email':'david@gmail.com'}]  
  
mail = Mail(app)  
 
@app.route("/")  
def index():  
    with mail.connect() as con:  
        for user in users:  
            message = "hello %s" %user['name']  
            msgs = Message(recipients=[user['email']],body = message, subject = 'hello', sender = 'david@gmail.com')  
            con.send(msgs)  
    return "Sent"  
if __name__ == "__main__":  
    app.run(debug = True)  
    
    
    
 ###############################################################
 #############################################################
 
 # Adding attachments with the mail
 
 
 # mailer_attach.py
 
 from flask import *  
from flask_mail import *  
  
app = Flask(__name__)  
  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465  
app.config["MAIL_USERNAME"] = 'admin@gmail.com'  
app.config['MAIL_PASSWORD'] = '********'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
  
mail = Mail(app)  
 
@app.route("/")  
def index():  
    msg = Message(subject = "hello", body = "hello", sender = "admin@gmail.com", recipients = ["ayush@javatpoint.com"])  
    with app.open_resource("/home/javatpoint/Desktop/galexy.jpg") as fp:  
        msg.attach("galexy.jpg","image/png",fp.read())  
        mail.send(msg)  
    return "sent"  
  
if __name__ == "__main__":  
    app.run(debug = True)  