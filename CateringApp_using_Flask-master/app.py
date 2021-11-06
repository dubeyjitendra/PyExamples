from flask import *
from db_connect import DB

obj = DB()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/validate', methods=["POST"])
def validate():
    try:
        value = read()
    except Exception as ex:
        print(ex)
    # print("email ", request.form['email'])
    # print("pass ", request.form['pass'])
    email =value[0][1]
    password= value[0][2]
    if request.form['email']== email and request.form['pass'] == password :
        return redirect(url_for("success"))
    return redirect(url_for("home"))


@app.route('/success')
def success():
    return render_template("welcome_to_my_page.html")
#
@app.route('/register')
def register():
    return render_template("register_page.html")

def read():
    c = obj.create_db()
    # create table in database using below way
    sql = """
            select * from login
          """
    # run the sql query
    cur = c.execute(sql)
    rows = cur.fetchall()
    login_info = []

    for i in rows:
        login_info.append(i)
    return login_info





if __name__ == '__main__':
    app.run(debug=False)