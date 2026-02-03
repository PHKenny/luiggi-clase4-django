import zoneinfo
from datetime import datetime
from typing import Self

from django.db import models

from luiggi.utils.uuid import Uuid

UTC = zoneinfo.ZoneInfo('UTC')


class User(models.Model):
  id = models.UUIDField(primary_key=True, editable=False, db_default=Uuid())

  username = models.CharField(max_length=150)
  encrypted_password = models.CharField(max_length=255)

  api_token = models.CharField(max_length=255)

  is_deleted = models.BooleanField(default=False)
  deleted_at = models.DateTimeField(null=True, blank=True)

  last_logged_at = models.DateTimeField(null=True, blank=True)

  class Meta:
    constraints = [
      models.UniqueConstraint(
        fields=['username'],
        condition=models.Q(is_deleted=False),
        name='%(app_label)s_%(class)s_username_uniq',
      ),
      models.UniqueConstraint(
        fields=['api_token'],
        condition=models.Q(is_deleted=False),
        name='%(app_label)s_%(class)s_api_token_uniq',
      ),
    ]

    indexes = [
      models.Index(
        fields=['username'],
        name='%(app_label)s_%(class)s_username_idx',
      ),
    ]

  def __str__(self: Self) -> str:
    return f'auth.User(id={self.id}, username={self.username})'

  @property
  def created_at(self: Self) -> datetime:
    if self.id.version != 7:
      raise ValueError('Cannot extract creation time from non-version 7 UUID')

    ts = self.id.int >> 80
    return datetime.fromtimestamp(ts / 1000, tz=UTC)

  @property
  def password(self: Self) -> str:
    return '[REDACTED]'

  @password.setter
  def password(self: Self, raw_password: str) -> None:
    from django.contrib.auth.hashers import make_password

    self.encrypted_password = make_password(raw_password)

  def is_valid_password(self: Self, raw_password: str) -> bool:
    from django.contrib.auth.hashers import check_password

    return check_password(raw_password, self.encrypted_password)
