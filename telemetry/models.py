from typing import Any, Self

from django.contrib.gis.db import models
from django.db.models import Func


class Uuid(Func):
  function = 'uuidv7'


class Now(Func):
  function = 'NOW'


class Telemetry(models.Model):
  id = models.UUIDField(primary_key=True, editable=False, db_default=Uuid())
  device_id = models.BigIntegerField()
  position = models.JSONField[dict[str, Any]](default=dict)
  payload = models.JSONField[dict[str, Any]](default=dict)
  sensors = models.JSONField[dict[str, Any]](default=dict)
  point_gis = models.PointField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    managed = False
    db_table = 'telemetry'

  def __str__(self: Self) -> str:
    return f'telemetry.Telemetry(id={self.id}, device_id={self.device_id})'
