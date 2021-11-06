############ Python Flask Tutorial #####################

### https://www.javatpoint.com/first-flask-application

#Flask is a web framework that provides libraries to build lightweight web applications in python.
#It is developed by Armin Ronacher who leads an international group of python enthusiasts (POCCO).

## What is WSGI?
#It is an acronym for web server gateway interface which is a standard for python web application development.
## It is considered as the specification for the universal interface between the web server and web application.


### First Flask application

from flask import Flask  
  
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/') #decorator defines the   
def home():  
    return "hello, this is our first flask website";  
  
if __name__ =='__main__':  
    app.run(debug = True)  
 
 
 ## Explain
 
 
 ### To build the python web application, we need to import the Flask module. An object of the Flask class is considered as the WSGI application
 
 ### We need to pass the name of the current module, i.e. __name__ as the argument into the Flask constructor.
 
 ### The route() function of the Flask class defines the URL mapping of the associated function. The syntax is given below.

 ###  app.route(rule, options) 

###  It accepts the following parameters.
 ### rule: 
    ### It represents the URL binding with the function.
    ### options: It represents the list of parameters to be associated with the rule object 
    
    
   #### The syntax is given below.

####  app.run(host, port, debug, options)  
