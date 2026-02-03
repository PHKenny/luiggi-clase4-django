from graphene import UUID, ObjectType, String


class User(ObjectType):
  id = UUID(description='Unique identifier of the user')
  username = String(description='Username of the user')
  api_token = String(description='API token of the user')
  password = String(description='[REDACTED] Password of the user')  # Always redacted
