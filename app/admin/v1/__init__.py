from typing import Final, cast
from flask_apispec import FlaskApiSpec
from flask_restful import Api
from flask import Blueprint, Flask

from app.admin.v1.user import UserResource, UsersResource

# Blueprint is a context of the application
api: Final[Api] = Api(Blueprint("admin_v1", "admin_v1", url_prefix="/admin/v1"))


def init_app(app: Flask, docs: FlaskApiSpec):
    app.register_blueprint(cast(Blueprint, api.blueprint))
    urls = [
        {"path": "/users/<uuid:id>", "resource": UserResource},
        {"path": "/users", "resource": UsersResource}
    ]

    for url in urls:
        api.add_resource(url["resource"], url["path"])
        docs.register(url["resource"], endpoint=url["resource"].__name__.lower(), blueprint=api.blueprint.name)