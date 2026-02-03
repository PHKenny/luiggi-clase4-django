from graphene import ID, Field, ObjectType, String


class Category(ObjectType):
  id = ID(description='ID of the category, on positive integer format')
  name = String(description='Name of the category')
  kind = Field('categories.graphql.enums.CategoryType', description='Kind of the category')
  description = String(description='Description of the category, can be NULL if is not supplied on creation')
