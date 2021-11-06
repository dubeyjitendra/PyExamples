from flask import *
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<html><head><title>First Html example</title></head>" \
           "<body><h1>Welcome to Hello World</h1></body></html>"

@app.route("/")
def call_by_html():
    return render_template("first.html")

### The jinga2 template engine provides the following delimiters to escape from the HTML.

####     {% ... %} for statements
####     {{ ... }} for expressions to print to the template output
####     {# ... #} for the comments that are not included in the template output
####     # ... ## for line statements

@app.route("/username/<user>")
def username(user):
    return render_template('message.html',name = user)

# if __name__ =='__main__':
#     app.run(debug=True)