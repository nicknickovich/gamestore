from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import (
    Game, User, Comment, Genre, OwnedGames, GamesByGenre
)


class GameSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        exclude = ("uuid",)
        load_instance = True


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ("uuid",)
        load_instance = True


class CommentSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        exclude = ("uuid",)
        include_fk = True
        load_instance = True
