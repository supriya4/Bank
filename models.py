from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

class Bank(db.Model):
    __tablename__= "bank"
    Name=db.Column(db.String,nullable=False)
    Code=db.Column(db.String,primary_key=True)
    Address=db.Column(db.String,nullable=False)
    Phone=db.Column(db.String,nullable=False)
    Branch=db.Column(db.String,nullable=False)
    City=db.Column(db.String,nullable=False)
