from typing import Self, cast

from graphene import Enum

from categories.enums import CategoryType as Source


class CategoryType(Enum):
  INGRESS = 'INGRESS'
  EGRESS = 'EGRESS'

  @property
  def description(self: Self) -> str:
    for v in Source.choices:
      if v[0] == self:
        return v[1]

    return f'Unknown CategoryType {self}'

  def __repr__(self: Self) -> str:
    return f'CategoryType.{self.value}'  # type: ignore

  def __str__(self: Self) -> str:
    return cast(str, self.value)  # type: ignore

  def __len__(self: Self) -> int:
    return len(self.value)  # type: ignore
