from typing import Any, Self

from django.core.management.base import BaseCommand

from categories.models import Category


class Command(BaseCommand):
  help = 'Manager of categories'

  def handle(self: Self, *args: Any, **kwargs: Any) -> None:
    cat = Category.objects.get(id=3)
    cat.description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
    cat.save()
    print(f'Categoría con ID {cat.id} actualizada.')
