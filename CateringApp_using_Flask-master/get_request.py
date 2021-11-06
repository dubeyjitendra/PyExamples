from flask import *

app = Flask(__name__)

@app.route('/')
def display():
    return render_template('login1.html')


@app.route('/login',methods =['GET'])
def login():
    uname = request.args.get('uname')
    password = request.args.get('pass')
    if uname =='XXXXX' and password =='XXXXX':
        return render_template('welcome.html')
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
