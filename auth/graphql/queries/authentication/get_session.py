from typing import Any, Self

from django.utils import timezone
from graphene import Field, ObjectType, String
from graphql import GraphQLResolveInfo

from auth.forms import SessionForm
from auth.models import User
from auth.utils.check_session import check_session
from luiggi.graphql.bases.query import BaseQuery
from luiggi.graphql.enums.status import Status


class GetSessionResponse(BaseQuery):
  result = Field('auth.graphql.entities.User')


class GetSession(ObjectType):
  get_session = Field(
    GetSessionResponse,
    api_token=String(required=True),
    description='Get the current user session based on the provided authentication token',
  )

  def resolve_get_session(self: Self, info: GraphQLResolveInfo, api_token: str) -> dict[str, Any]:
    errors, u = check_session(api_token=api_token)
    if errors:
      return errors

    return {'status': Status.OK, 'result': u}
