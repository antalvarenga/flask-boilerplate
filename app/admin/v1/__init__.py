from typing import Final, List, cast

from flask import Blueprint, Flask
from flask_apispec import FlaskApiSpec
from flask_restful import Api

from app.admin.v1.user import UserResource, UsersResource
from app.types import TBlueprintUrl

# Blueprint is a context of the application
api: Final[Api] = Api(Blueprint("admin_v1", "admin_v1", url_prefix="/admin/v1"))


def init_app(app: Flask, docs: FlaskApiSpec):
    app.register_blueprint(cast(Blueprint, api.blueprint))
    urls: List[TBlueprintUrl] = [
        {"path": "/users/<uuid:id>", "resource": UserResource},
        {"path": "/users", "resource": UsersResource},
    ]

    for url in urls:
        api.add_resource(url["resource"], url["path"])
        docs.register(
            url["resource"],
            endpoint=url["resource"].__name__.lower(),
            blueprint=api.blueprint.name,
        )
