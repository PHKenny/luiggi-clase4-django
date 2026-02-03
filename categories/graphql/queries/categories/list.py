from typing import Any, Self

from graphene import Field, List, ObjectType, String
from graphql import GraphQLResolveInfo

from auth.utils.check_session import check_session
from categories.models import Category
from luiggi.graphql.bases.query import BaseQuery
from luiggi.graphql.enums.status import Status


class CategoriesResponse(BaseQuery):
  result = List('categories.graphql.entities.Category')


class CategoriesList(ObjectType):
  categories = Field(
    CategoriesResponse,
    api_token=String(required=True),
    description='Get a list of categories',
  )

  def resolve_categories(self: Self, info: GraphQLResolveInfo, api_token: str) -> dict[str, Any]:
    errors, _ = check_session(api_token=api_token)
    if errors:
      return errors

    return {
      'status': Status.OK,
      'result': Category.objects.all().order_by('id'),
    }
