from graphene import ObjectType, Schema

from auth.graphql.mutations.authentication import Login
from auth.graphql.queries.authentication import GetSession
from categories.graphql.mutations.categories import UpsertCategoryMutation
from categories.graphql.queries.categories import CategoriesList


class Queries(
  GetSession,
  CategoriesList,
  ObjectType,
): ...


class Mutations(
  Login,
  UpsertCategoryMutation,
  ObjectType,
): ...


schema = Schema(query=Queries, mutation=Mutations)
