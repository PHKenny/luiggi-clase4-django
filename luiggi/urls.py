from django.urls import path
from graphene_django.views import GraphQLView

from luiggi.graphql.schema import schema
from luiggi.views import index, say_hello

urlpatterns = [
  path('', index, name='index'),
  path('hello', say_hello, name='say_hello'),
  path('hello/<name>', say_hello, name='say_hello'),
  path(
    'graphql',
    GraphQLView.as_view(graphiql=False, schema=schema),
  ),
]
