from django.db.models import Func


class Uuid(Func):
  function = 'uuidv7'
