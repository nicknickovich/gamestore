from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import (
    Game, User, Comment, Genre, OwnedGames, GamesByGenre
)


class GameSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        load_instance = True


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ("uuid",)
        load_instance = True


class CommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True


class GenreSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Genre
        load_instance = True


class OwnedGamesSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = OwnedGames
        load_instance = True


class GamesByGenreSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = GamesByGenre
        load_instance = True
