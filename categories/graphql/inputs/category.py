from graphene import ID, Field, InputObjectType, String


class CategoryInput(InputObjectType):
  id = ID(
    description='ID of the category, on positive integer format. If is not supplied, a new category will be created',
    default_value=None,
  )
  name = String(
    description='Name of the category',
    required=True,
  )
  kind = Field(
    'categories.graphql.enums.CategoryType',
    description='Kind of the category',
    required=True,
  )
  description = String(
    description='Description of the category, can be NULL if is not supplied on creation',
    required=True,
  )
