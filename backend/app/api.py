from flask import Blueprint, request
from flask_restful import Resource
from app import api_restful, db, schemas
from app.models import User


api = Blueprint("api", __name__)
user_schema = schemas.UserSchema()


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