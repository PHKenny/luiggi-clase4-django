from typing import Any, Self

from django.utils import timezone
from graphene import Field, Mutation, ObjectType, String
from graphql import GraphQLResolveInfo

from auth.forms import LoginForm
from auth.models import User
from luiggi.graphql.enums import Status


class LoginMutation(Mutation):
  """Mutation to log in a user."""

  class Arguments:
    username = String(required=True)
    password = String(required=True)

  status = Field(Status, description='Status of the login attempt')
  errors = Field('luiggi.graphql.scalars.Json', description='Errors encountered during login')
  result = Field('auth.graphql.entities.User')

  def mutate(self: Self, info: GraphQLResolveInfo, username: str, password: str) -> dict[str, Any]:
    f = LoginForm({'username': username, 'password': password})
    if not f.is_valid():
      return {'status': Status.BAD_REQUEST, 'errors': f.errors()}

    try:
      u = User.objects.get(username=username, is_deleted=False)
    except User.DoesNotExist:
      return {'status': Status.BAD_REQUEST, 'errors': {'__all__': ['Invalid username or password.']}}

    if not u.is_valid_password(password):
      return {'status': Status.BAD_REQUEST, 'errors': {'__all__': ['Invalid username or password.']}}

    u.last_logged_at = timezone.now()
    u.save(update_fields=['last_logged_at'])

    u.refresh_from_db()

    return {'status': Status.OK, 'result': u}


class Login(ObjectType):
  login = LoginMutation.Field()
