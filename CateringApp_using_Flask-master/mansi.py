from flask import *
app=Flask(__name__)


@app.route("/")
def Registration_form():
    return render_template("registration.html")

@app.route("/validate",methods=["POST"])
def info():
    if request.method=="POST":
        username= request.form['name']
        email=request.form['email']
        address=request.form['add']
        if username=="XXXXX" and email=="XXXXXXXX@gmail.com" and address=="XXXXX":
            return("registration complete")
        else:
            return render_template("error1.html")



if __name__ == '__main__':
    app.run(debug=True)

