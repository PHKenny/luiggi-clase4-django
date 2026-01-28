from typing import Any, Self

from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
  help = 'Obtiene el promedio de velocidad de todos los dispositivos'

  def handle(self: Self, *args: Any, **options: Any) -> None:
    total_speed = 0.0
    count = 0

    with connection.cursor() as cur:
      cur.execute("""
        SELECT
          (position->'speed')::double precision AS speed
        FROM telemetry_telemetry
        WHERE id >= to_uuidv7_boundary('2025-01-03 12:00:00-06')
          AND id <= to_uuidv7_boundary('2025-01-04 00:00:00-06');
      """)
      rows = cur.fetchall()

    for row in rows:
      speed = row[0]
      if speed is not None:
        total_speed += speed
        count += 1

    avg_speed = total_speed / count if count > 0 else 0.0
    self.stdout.write(f'Promedio de velocidad: {avg_speed:.2f}')
