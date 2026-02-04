import random
from typing import Any, Self

from django.core.management.base import BaseCommand

from categories.models import Category
from movements.models import Movement


class Command(BaseCommand):
  def handle(self: Self, *args: Any, **options: Any) -> None:
    categories = list(Category.objects.all())

    for _ in range(1_000):
      category = random.choice(categories)

      amount = random.uniform(1000, 5000)
      if category.kind == 'EGRESS':
        amount = -amount

      Movement.objects.create(
        amount=amount,
        category=category,
      )
