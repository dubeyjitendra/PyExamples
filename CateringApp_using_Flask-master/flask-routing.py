from flask import Flask

app = Flask(__name__)


def display():
    return "I am display function"


app.add_url_rule("/display","display", display)





if __name__=='__main__':
    app.run(debug=True)