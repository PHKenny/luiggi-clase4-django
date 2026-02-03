from typing import Any, Self

from django.utils import timezone
from graphene import Argument, Field, ObjectType, String
from graphql import GraphQLResolveInfo

from auth.utils.check_session import check_session
from categories.forms import CategoryForm
from categories.models import Category
from luiggi.graphql.bases.mutation import BaseMutation
from luiggi.graphql.enums import Status


class UpsertCategory(BaseMutation):
  """Mutation to create or update a category."""

  class Arguments:
    api_token = String(required=True)
    data = Argument(
      'categories.graphql.inputs.CategoryInput',
      required=True,
      description='Data for creating or updating a category',
    )

  result = Field('categories.graphql.entities.Category')

  def mutate(self: Self, info: GraphQLResolveInfo, **args: Any) -> dict[str, Any]:
    api_token = args.get('api_token')
    if not api_token:
      return {'status': Status.BAD_REQUEST}

    errors, _ = check_session(api_token=api_token)
    if errors:
      return errors

    f = CategoryForm(args.get('data'))
    if not f.is_valid():
      return {'status': Status.BAD_REQUEST, 'errors': f.errors()}

    if pk := args['data'].get('id'):
      try:
        c = Category.objects.get(pk=pk)
      except Category.DoesNotExist:
        return {'status': Status.BAD_REQUEST}

      c.name = args['data']['name']
      c.description = args['data'].get('description', c.description)
      c.kind = args['data']['kind']
      c.save()
    else:
      c = Category.objects.create(
        name=args['data']['name'],
        description=args['data'].get('description', 'N/A'),
        kind=args['data']['kind'],
      )

    return {'status': Status.OK, 'result': c}


class UpsertCategoryMutation(ObjectType):
  upsert_category = UpsertCategory.Field()
