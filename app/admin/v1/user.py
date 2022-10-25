from functools import cached_property
from flask import abort
from flask_apispec import MethodResource, doc, marshal_with, use_kwargs
from app.admin.v1.schemas.user import PostUserSchema, UserSchema

from app.services.user import UserService

@doc(description="User of the app", tags=["admin/users"])
class UserResource(MethodResource):
    @cached_property
    def service(self):
        return UserService()

    @marshal_with(UserSchema)
    def get(self, id):
        user = self.service.get_by_id(id)
        return user if user else abort(404)

    # @marshal_with(UserSchema)
    # @use_kwargs(PutUserSchema, location="json")
    # def put(self, id, **data):
    #     user = self.service.update(id, **data)
    #     return user


@doc(description="Users of the app", tags=["admin/users"])
class UsersResource(MethodResource):
    @cached_property
    def service(self):
        return UserService()

    @marshal_with(UserSchema)
    @use_kwargs(PostUserSchema, location="json")
    def post(self, **data):
        user = self.service.create(**data)
        return user

    # @marshal_with(UserSchema)
    # @use_kwargs(PutUserSchema, location="json")
    # def put(self, id, **data):
    #     user = self.service.update(id, **data)
    #     return user
