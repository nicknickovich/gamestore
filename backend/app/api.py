from flask import Blueprint, request
from flask_restful import Resource
from app import api_restful, db, schemas
from app.models import User, Game


api = Blueprint("api", __name__)
user_schema = schemas.UserSchema()
game_schema = schemas.GameSchema()


class UserRoutes(Resource):
    def get(self, id=None):
        if id is None:
            users = User.query.all()
            return user_schema.dump(users, many=True)
        user = User.query.get_or_404(id)
        return user_schema.dump(user)
    
    def post(self):
        new_user = user_schema.load(request.json, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201

    def put(self, id):
        user = User.query.get_or_404(id)
        updated_user = user_schema.load(
            request.json, instance=user, session=db.session
        )
        db.session.commit()
        return user_schema.dump(updated_user)

    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return "", 204

api_restful.add_resource(
    UserRoutes,
    "/api/users",
    "/api/users/<id>"
)


class GameRoutes(Resource):
    def get(self, id=None):
        if id is None:
            games = Game.query.all()
            return game_schema.dump(games, many=True)
        game = Game.query.get_or_404(id)
        return game_schema.dump(game)

    def post(self):
        new_game = game_schema.load(request.json, session=db.session)
        db.session.add(new_game)
        db.session.commit()
        return game_schema.dump(new_game), 201

    def put(self, id):
        game = Game.query.get_or_404(id)
        updated_game = game_schema.load(
            request.json, instance=game, session=db.session
        )
        db.session.commit()
        return game_schema.dump(updated_game)

    def delete(self, id):
        game = Game.query.get_or_404(id)
        db.session.delete(game)
        db.session.commit()
        return "", 204


api_restful.add_resource(
    GameRoutes,
    "/api/games",
    "/api/games/<id>"
)
