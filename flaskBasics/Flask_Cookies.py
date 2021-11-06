################ Flask Cookies #################################

### The cookies are stored in the form of text files on the client's machine. 
### Cookies are used to track the user's activities on the web and reflect some suggestions according to the user's choices to enhance the user's experience.


#### Cookies are set by the server on the client's machine which will be associated with the client's request to that particular server
#### in all future transactions until the lifetime of the cookie expires or it is deleted by the specific web page on the server.

### In flask, the cookies are associated with the Request object as the dictionary object of all the cookie variables and their values
###  transmitted by the client. Flask facilitates us to specify the expiry time, path, and the domain name of the website.



### Syntax

# response.setCookie(<title>, <content>, <expiry time>)  





#### we can read the cookies stored on the client's machine using the get() method of the cookies attribute associated with the Request object.

## Syntax

### request.cookies.get(<title>)  

# Example

from flask import *  
  
app = Flask(__name__)  
 
@app.route('/cookie')  
def cookie():  
    res = make_response("<h1>cookie is set</h1>")  
    res.set_cookie('foo','bar')  
    return res  
  
if __name__ == '__main__':  
    app.run(debug = True)



# We can track the cookie details in the content settings of the browser as given in below image.
# https://static.javatpoint.com/tutorial/flask/images/flask-cookies2.png