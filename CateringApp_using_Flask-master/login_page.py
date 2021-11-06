from flask import *
app=Flask(__name__)


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/",methods=["POST"])
def success():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pass']

    if password == "XXXXX":
        resp = make_response(render_template('success.html'))
        resp.set_cookie('emailkey', email)
        return resp
    else:
        return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)
