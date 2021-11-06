############ Flask App routing #####################

## Example

from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home')  
def home():  
    return "hello, welcome to our website";  
  
if __name__ =="__main__":  
    app.run(debug = True)  
    
    
    
    
    
### Example 2

from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home/<name>')  
def home(name):  
    return "hello,"+name;  
  
if __name__ =="__main__":  
    app.run(debug = True)  
    
    
    
    
 ### Example 3
 
from flask import Flask  
app = Flask(__name__)  
 
@app.route('/home/<int:age>')  
def home(age):  
    return "Age = %d"%age;  
  
if __name__ =="__main__":  
    app.run(debug = True)  
    
    
 

### The add_url_rule() function 


###  There is one more approach to perform routing for the flask web application that can be done by using the add_url() function of the Flask class.
###  The syntax to use this function is given below.

## Syntax
###  add_url_rule(<url rule>, <endpoint>, <view function>)  

### Example

from flask import Flask  
app = Flask(__name__)  
  
def about():  
    return "This is about page";  
  
app.add_url_rule("/about","about",about)  
  
if __name__ =="__main__":  
    app.run(debug = True)  
    
    
 

