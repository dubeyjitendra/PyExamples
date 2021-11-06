from flask import *

app = Flask(__name__)

@app.route('/')
def display():
    return render_template('login1.html')


@app.route('/login',methods =['POST'])
def login():
    uname = request.form['uname']
    password = request.form['pass']
    if uname =='XXXXX' and password =='XXXXX':
        return render_template('welcome.html')
    else:
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
