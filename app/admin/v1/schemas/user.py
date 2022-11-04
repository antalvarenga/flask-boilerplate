from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from app.models.user import User


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User


class PostUserSchema(UserSchema):
    class Meta(UserSchema.Meta):
        exclude = ("id",)
