from typing import TYPE_CHECKING, Self

from django.db import models

if TYPE_CHECKING:
  from categories.models import Category


class Movement(models.Model):
  if TYPE_CHECKING:
    category_id: int | None

  id = models.BigAutoField(primary_key=True)
  amount = models.DecimalField(max_digits=10, decimal_places=3, db_comment='Movement amount')
  when = models.DateTimeField(db_comment='Movement date and time', auto_now_add=True)
  category = models.ForeignKey['Category'](
    'categories.Category',
    on_delete=models.SET_NULL,
    null=True,
    related_name='movements',
  )

  def __str__(self: Self) -> str:
    return f'movements.Movement(id={self.id})'
