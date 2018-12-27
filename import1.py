import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:ilovemeow16@@localhost:5432/bankdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("bank.csv")
    reader = csv.reader(f)
    for Name,Code,Address,Phone,Branch,City in reader:
        bank = Bank(Name=Name,Code=Code,Address=Address,Phone=Phone,Branch=Branch,City=City)
        db.session.add(bank)
        print("Added Rows")

    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
