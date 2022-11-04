from typing import Type, TypedDict

from flask_apispec import MethodResource


class TBlueprintUrl(TypedDict):
    path: str
    resource: Type[MethodResource]
