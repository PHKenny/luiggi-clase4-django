from graphene import Field, ObjectType


class BaseQuery(ObjectType):
  status = Field('luiggi.graphql.enums.Status', description='Status of the query')
  errors = Field('luiggi.graphql.scalars.Json', description='Errors encountered during the query')
