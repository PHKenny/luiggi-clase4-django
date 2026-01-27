from typing import TYPE_CHECKING, Self

from django.db import models

from categories.enums import CategoryType

if TYPE_CHECKING:
  from django.db.models.manager import RelatedManager

  from movements.models import Movement


class Category(models.Model):
  if TYPE_CHECKING:
    movements = RelatedManager['Movement']()

  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=255, db_comment='Category name')
  kind = models.CharField(
    max_length=7,
    choices=CategoryType.choices,
    db_default=CategoryType.EGRESS,
  )
  description = models.TextField(db_default='N/A', db_comment='Category description')

  def __str__(self: Self) -> str:
    return f'categories.Category(id={self.id}, name="{self.name}")'
