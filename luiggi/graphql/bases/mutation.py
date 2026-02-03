from typing import Any, Self

from graphene import Field, Mutation
from graphql import GraphQLResolveInfo


class BaseMutation(Mutation):
  status = Field('luiggi.graphql.enums.Status', description='Status of the mutation')
  errors = Field('luiggi.graphql.scalars.Json', description='Errors encountered during the mutation')

  def mutate(self: Self, info: GraphQLResolveInfo, **args: Any) -> dict[str, Any]:
    return {'status': 'NOT_IMPLEMENTED', 'errors': {'__all__': ['This mutation is not implemented.']}}
