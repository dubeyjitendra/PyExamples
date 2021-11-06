from flask import Flask

# create the flask object
app = Flask(__name__)

@app.route("/")
def age():
    return "I am flask developer"

@app.route("/path")
def login():
    return "This is my First Web app in flask"

@app.route("/pname/<string:name>/")
def record(name):
    return "Name %s"%name


# if __name__=='__main__':
#     app.run(debug=True)


