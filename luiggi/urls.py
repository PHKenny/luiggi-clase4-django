from django.urls import path

from luiggi.views import index, say_hello

urlpatterns = [
  path('', index, name='index'),
  path('hello/', say_hello, name='say_hello'),
  path('hello/<name>/', say_hello, name='say_hello'),
]
