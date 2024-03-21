from celery.result import AsyncResult
from flask_apispec import MethodResource, doc, use_kwargs
from marshmallow import fields

from app.tasks import add


@doc(description="Adds asynchronously", tags=["api/celery"])
class CeleryPostResource(MethodResource):
    @use_kwargs({"a": fields.Int(), "b": fields.Int()})
    def post(self, **data):
        result = add.delay(data["a"], data["b"])
        return {"result_id": result.id}


@doc(description="Adds asynchronously", tags=["api/celery"])
class CeleryGetResource(MethodResource):
    def get(self, id):
        result = AsyncResult(id)

        return {
            "ready": result.ready(),
            "successful": result.successful(),
            "value": result.result if result.ready() else None,
        }
