###############  Flask Templates ########################

### we have returned the simple string as the response from the view function. Although, flask facilitates us to return 
### the response in the form of HTML templates. In this section of the tutorial,
### we will go through the ways using which we can return the HTML response from the web applications.

### Example

## script.py

from flask import *  
app = Flask(__name__)  
@app.route('/')  
def message():  
      return "<html><body><h1>Hi, welcome to the website</h1></body></html>"  
      
if __name__ == '__main__':  
   app.run(debug = True)  



### Rendering external HTML files

### Example

## To render an HTML file from the view function, let's first create an HTML file named as message.html.

#message.html

<html>  
<head>  
<title>Message</title>  
</head>  
<body>  
<h1>hi, welcome to the website </h1>  
</body>  
</html>  

# script.py

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def message():  
      return render_template('message.html')  
if __name__ == '__main__':  
   app.run(debug = True)  
   
   
   
   
####  Delimiters

## Jinga 2 template engine provides some delimiters which can be used in the HTML to make it capable of dynamic data representation.

### The jinga2 template engine provides the following delimiters to escape from the HTML.

####     {% ... %} for statements
####     {{ ... }} for expressions to print to the template output
####     {# ... #} for the comments that are not included in the template output
####     # ... ## for line statements



## Example

##  message.html

<html>  
<head>  
<title>Message</title>  
</head>  
<body>  
<h1>hi, {{ name }}</h1>  
</body>  
</html>  


## script.py

from flask import *  
app = Flask(__name__)  
  
@app.route('/user/<uname>')  
def message(uname):  
      return render_template('message.html',name=uname)  
      
if __name__ == '__main__':  
   app.run(debug = True)  






### Embedding Python statements in HTML

# Example

# script.py

from flask import *  
app = Flask(__name__)  
  
@app.route('/table/<int:num>')  
def table(num):  
      return render_template('print-table.html',n=num)  
if __name__ == '__main__':  
   app.run(debug = True)  
   
   
 # print-table.html
 
<html>  
<head>  
<title>print table</title>  
</head>  
<body>  
<h2> printing table of {{n}}</h2>  
{% for i  in range(1,11): %}  
    <h3>{{n}} X {{i}} = {{n * i}} </h3>  
{% endfor %}  
</body>  
</html>  





### Referring Static files in HTML

## script.py

from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def message():  
      return render_template('message.html')  
if __name__ == '__main__':  
   app.run(debug = True)  
   
   
 ## message.html
 
 <html>  
<head>  
    <title>Message</title>  
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">  
</head>  
   
<body>  
    <h1>hi, welcome to the website</h1>  
</body>  
</html>


## style.css

body {  
  background-color: powderblue;  
}  
h1 {  
  color: blue;  
}  
p {  
  color: red;  
}  





