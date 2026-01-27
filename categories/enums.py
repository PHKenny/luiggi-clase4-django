from django.db import models


class CategoryType(models.TextChoices):
  # ON_PYTHON = ON_POSTGRES, Public message
  INGRESS = 'INGRESS', 'Ingress type'
  EGRESS = 'EGRESS', 'Egress type'
