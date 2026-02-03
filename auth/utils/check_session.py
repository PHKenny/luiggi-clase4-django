from typing import Any

from django.utils import timezone

from auth.forms import SessionForm
from auth.models import User
from luiggi.graphql.enums.status import Status


def check_session(*, api_token: str) -> tuple[dict[str, Any], None] | tuple[None, User]:
  f = SessionForm({'token': api_token})
  if not f.is_valid():
    return {'status': Status.BAD_REQUEST, 'errors': f.errors()}, None

  try:
    u = User.objects.get(api_token=api_token, is_deleted=False)
  except User.DoesNotExist:
    return {'status': Status.BAD_REQUEST, 'errors': {'__all__': ['Invalid or expired token.']}}, None

  u.last_logged_at = timezone.now()
  u.save(update_fields=['last_logged_at'])
  u.refresh_from_db()

  return None, u
