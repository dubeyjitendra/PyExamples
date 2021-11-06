# WTF stands for WT Forms which is intended to provide the interactive user interface for the user. The WTF is a built-in module of the flask which provides an alternative way of designing forms in the flask web applications.
# Why WTF Useful?
# WTF is useful due to the following factors.

    # The form elements are sent along with the request object from the client side to the server side. Server-Side script needs to recreate the form elements since there is no direct mapping between the client side form elements and the variables to be used at the server side.
    # There is no way to render the HTML form data at real time.
    # The WT Forms is a flexible, form rendering, and validation library used to provide the user interface.
    

# Install Flask-WTF
#### pip install flask-wtf 


# 1	TextField	    It is used to represent the text filed HTML form element.
# 2	BooleanField	It is used to represent the checkbox HTML form element.
# 3	DecimalField	It is used to represent the text field to display the numbers with decimals.
# 4	IntegerField	It is used to represent the text field to display the integer values.
# 5	RadioField	    It is used to represent the radio button HTML form element.
# 6	SelectField	    It is used to represent the select form element.
# 7	TextAreaField	It is used to represent text area form element.
# 8	PasswordField	It is used to take the password as the form input from the user.
# 9	SubmitField	    It provides represents the <input type = 'submit' value = 'Submit'> html form element.


# forms.py

from flask_wtf import Form  
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField  
from wtforms import validators, ValidationError  
  
class ContactForm(Form):  
   name = TextField("Candidate Name ",[validators.Required("Please enter your name.")])  
   Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])  
   Address = TextAreaField("Address")  
     
   email = TextField("Email",[validators.Required("Please enter your email address."),  
   validators.Email("Please enter your email address.")])  
     
   Age = IntegerField("Age")  
   language = SelectField('Programming Languages', choices = [('java', 'Java'),('py', 'Python')])  
  
   submit = SubmitField("Submit")  
   
   
# formexample.py
from flask import Flask, render_template, request, flash  
from forms import ContactForm  
app = Flask(__name__)  
app.secret_key = 'development key'  
 
@app.route('/contact', methods = ['GET', 'POST'])  
def contact():  
   form = ContactForm()  
   if form.validate() == False:  
      flash('All fields are required.')  
   return render_template('contact.html', form = form)  
 
 
 
@app.route('/success',methods = ['GET','POST'])  
def success():  
   return render_template("success.html")  
  
if __name__ == '__main__':  
   app.run(debug = True) 


# contact.html
<!doctype html>  
<html>  
   <body>  
      <h2 style = "text-align: center;">Registration Form</h2>  
          
      {% for message in form.name.errors %}  
         <div>{{ message }}</div>  
      {% endfor %}  
        
      {% for message in form.email.errors %}  
         <div>{{ message }}</div>  
      {% endfor %}  
        
      <form action = "http://localhost:5000/success" method = "POST">  
           
            {{ form.hidden_tag() }}  
              
            <div style = "font-size:18px;" font-weight:bold; margin-left:150px;>  
               {{ form.name.label }}<br>  
               {{ form.name }}  
               <br>  
               {{ form.Gender.label }} {{ form.Gender }}  
               {{ form.Address.label }}<br>  
               {{ form.Address }}  
               <br>  
               {{ form.email.label }}<br>  
               {{ form.email }}  
               <br>  
               {{ form.Age.label }}<br>  
               {{ form.Age }}  
               <br>  
               {{ form.language.label}}<br><br>  
               {{ form.language }}  
               <br><br>  
               {{ form.submit }}  
            </div>  
              
         </fieldset>  
      </form>  
   </body>  
</html>  


# Success.html
<!DOCTYPE html>  
<html>  
<head>  
    <title></title>  
</head>  
<body>  
<h1>Form posted successfully</h1>  
</body>  
</html>    