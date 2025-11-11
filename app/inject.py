
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) 
from db_models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

db.init_app(app)
with app.app_context():
    db.create_all()

with app.app_context():
    admin = User(name="barnabas", email='banabasmwesigye3@gmail.com', phone='0771169165', password="100Billion$")
    db.session.add(admin)
    db.session.commit()
with app.app_context():
    print(User.query.all())
