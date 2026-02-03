from typing import Self, cast

from graphene import Enum


class Status(Enum):
  OK = 'OK'
  BAD_REQUEST = 'BAD_REQUEST'
  INTERNAL_ERROR = 'INTERNAL_ERROR'

  I_AM_TEAPOT = 'I_AM_A_TEAPOT'

  @property
  def description(self: Self) -> str:
    match self:
      case Status.OK:
        return 'The request has succeeded'
      case Status.BAD_REQUEST:
        return 'The server could not understand the request due to invalid syntax'
      case Status.INTERNAL_ERROR:
        return 'The server has encountered a situation it does not know how to handle'
      case Status.I_AM_TEAPOT:
        return 'The server refuses to brew coffee because it is a teapot'

      case _:
        return f'Unknown Status {self}'

  def __repr__(self: Self) -> str:
    return f'Status.{self.value}'  # type: ignore

  def __str__(self: Self) -> str:
    return cast(str, self.value)  # type: ignore

  def __len__(self: Self) -> int:
    return len(self.value)  # type: ignore
