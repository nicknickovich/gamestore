from flask import Blueprint
from flask_restful import Resource
from app import api_restful
from app.models import User


api = Blueprint("api", __name__)


class BasicRoutes(Resource):
    def get(self, id=None):
        if id is None:
            return {"message": "get all"}
        return {"message": f"get one with id={id}"}

api_restful.add_resource(
    BasicRoutes,
    "/api/users",
    "/api/users/<int:id>"
)
