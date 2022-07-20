from flask import Flask, render_template
from forms import HomeForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '9kah283hdjialksuen8366d38maop'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mafiaparty.db'
db = SQLAlchemy(app)

""" Setting up the database """

"""Model for active rooms"""


class Room(db.Model):
    code = db.Column(db.String, unique=True, primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=True)


"""Model for users"""


class User(db.Model):
    cookie = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)


"""Table to keep track of what users are in what rooms"""
room_members = db.Table(
    'room_members',
    db.Column('user', db.String, db.ForeignKey('user.cookie')),
    db.Column('room', db.String, db.ForeignKey('room.code'))
    )

db.create_all()
db.session.add(Room(code="TEST01"))

try:
    db.session.commit()
except Exception as e:
    db.session.rollback()


@app.route("/")
def homepage():
    form = HomeForm()
    return render_template("home.html", form=form)


@app.route("/game/<code>")
def game(code):
    room = Room.query.get(code)
    return render_template("game.html", room=room)


if __name__ == "__main__":
    app.run()
