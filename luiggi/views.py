from django.http import HttpRequest, JsonResponse


def index(request: HttpRequest) -> JsonResponse:
  return JsonResponse({'message': 'Welcome to Luiggi!'})


def say_hello(request: HttpRequest, name: str = '') -> JsonResponse:
  if name:
    return JsonResponse({'message': f'Hello, {name}!'})

  return JsonResponse({'message': 'Hello, world!'})
