from typing import Any, Self

from django.core.management.base import BaseCommand

from categories.models import Category


class Command(BaseCommand):
  help = 'Manager of categories'

  def handle(self: Self, *args: Any, **kwargs: Any) -> None:
    name = input('Ingrese el nombre de la categoría: ')
    description = input('Ingrese descripción [Default: N/A]: ')
    if not description:
      description = 'N/A'

    cat = Category.objects.create(name=name, description=description)
    print(f'Categoría creada con ID: {cat.id}')
