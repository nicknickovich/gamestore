import uuid
import datetime
from werkzeug.security import generate_password_hash
from app import db


class Game(db.Model):
    __tablename__ = "game"
    uuid = db.Column(db.String(36), unique=True, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    price = db.Column(db.Float)
    cover_image = db.Column(db.String(255))
    description = db.Column(db.Text)
    hidden = db.Column(db.Boolean)

    def __init__(self, name, price, cover_image, description):
        self.name = name
        self.price = price
        self.cover_image = cover_image
        self.description = description
        self.uuid = str(uuid.uuid4())
        self.hidden = False

    def __repr__(self):
        return f"Game({self.name, self.uuid})"


class User(db.Model):
    __tablename__ = "user"
    uuid = db.Column(db.String(36), unique=True, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    account_created = db.Column(db.DateTime)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    is_stuff = db.Column(db.Boolean)

    def __init__(self, email, first_name, last_name, username, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = generate_password_hash(password)
        self.uuid = str(uuid.uuid4())
        self.account_created = datetime.datetime.utcnow()
        self.is_stuff = False

    def __repr__(self):
        return f"User({self.first_name} {self.last_name}, {self.email})"


class Comment(db.Model):
    __tablename__ = "comment"
    uuid = db.Column(db.String(36), unique=True, primary_key=True)
    user_id = db.Column(db.String(36), db.ForeignKey("user.uuid"))
    game_id = db.Column(db.String(36), db.ForeignKey("game.uuid"))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

    def __init__(self, user_id, game_id, content):
        self.uuid = str(uuid.uuid4())
        self.user_id = user_id
        self.game_id = game_id
        self.content = content
        self.date_posted = datetime.datetime.utcnow()


class Genre(db.Model):
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.String(255)

    def __init__(self, id, name):
        self.id = id
        self.name = name


class OwnedGames(db.Model):
    __tablename__ = "ownedgames"
    user_id = db.Column(db.String(36), db.ForeignKey("user.uuid"), primary_key=True)
    game_id = db.Column(db.String(36), db.ForeignKey("game.uuid"), primary_key=True)

    def __init__(self, user_id, game_id):
        self.user_id = user_id
        self.game_id = game_id


class GamesByGenre(db.Model):
    __tablename__ = "gamesbygenre"
    game_id = db.Column(db.String(36), db.ForeignKey("game.uuid"), primary_key=True)
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"), primary_key=True)

    def __init__(self, game_id, genre_id):
        self.game_id = game_id
        self.genre_id = genre_id
