from flask import Flask,render_template,request
from models import *
from flask import jsonify
from sqlalchemy import and_

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:ilovemeow16@@localhost:5432/bankdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")
@app.route("/serve",methods=['GET','POST'])
def serve():
    name=request.form.get("code")
    print(name)
    ba=Bank.query.filter_by(Code=name).all()
    if not ba:
        return render_template("error.html")
    db.session.commit()
    return render_template("flight.html",ba=ba)
@app.route("/details",methods=['GET','POST'])
def details():
    name=request.form.get("name")
    city=request.form.get("city")
    ba=Bank.query.filter(and_(Bank.Name==name,Bank.City==city))
    if not ba:
        return render_template("error.html")
    db.session.commit()
    return render_template("flight.html",ba=ba)


if __name__=='__main__':
    app.run(debug=True)
