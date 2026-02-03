from typing import Any

from graphene.types import Scalar
from graphene.types.scalars import MAX_INT, MIN_INT
from graphql.language import ast


class Json(Scalar):
  """JSON object scalar"""

  @staticmethod
  def coerce_json(value: dict[str, Any], _variables: Any = None) -> dict[str, Any]:
    """Validate JSON"""
    return value

  serialize = coerce_json
  parse_value = coerce_json

  @staticmethod
  def parse_literal(value: ast.ValueNode, _variables: Any = None) -> Any:
    """Parse literal"""
    if isinstance(value, (ast.StringValueNode, ast.BooleanValueNode)):
      return value.value

    if isinstance(value, ast.IntValueNode):
      num = int(value.value)
      if MIN_INT <= num <= MAX_INT:
        return num

    if isinstance(value, ast.FloatValueNode):
      return float(value.value)

    if isinstance(value, ast.ListValueNode):
      return [Json.parse_literal(value) for value in value.values]

    if isinstance(value, ast.ObjectValueNode):
      return {field.name.value: Json.parse_literal(field.value) for field in value.fields}

    return None
