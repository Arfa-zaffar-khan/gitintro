

from flask import *
from dbm import *

app=Flask(__name__,static_folder="static")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register")
def reg():
    return render_template("register.html")

@app.route("/details")
def details():
    d=showdata()
    return render_template("details.html",ulist=d)
@app.route("/log")
def lg():
    return render_template("login.html")

@app.route("/insertdata",methods=["post"])
def insertdata():
    name=request.form["username"]
    city=request.form["usercity"]
    email=request.form["useremail"]
    password=request.form["userpassword"]
    t=(name,city,email,password)
    insert(t)
    return redirect("/")

@app.route("/edit")
def edit():
    email=request.args.get("email")
    data=editdetails(email)
    return render_template("edit.html",t=data[0])

@app.route("/updatedata",methods=["post"])
def updatedata():
    name=request.form["username"]
    city=request.form["usercity"]
    email=request.form["useremail"]
    password=request.form["userpassword"]
    t=(name,city,email,password,email)
    update(t)
    return redirect("/details")

@app.route("/delete")
def delete():
    email=request.args.get("email")
    drop(email)
    return redirect("/details")

@app.route("/login",methods=["post"])
def log():
    email=request.form["email"]
    password=request.form["password"]
    t=check(email)
    t1=(email,password)
    if t1 in t:
        return redirect("/details")
    else:
        return redirect("/log")

if __name__=='__main__':
    app.run(debug=True)

#changes
