from typing import Any

def test(*args: Any, **kwargs: Any) -> None:
  print(f'{args=} - {kwargs=}')


test(1, 2, 3, 4, 5, test=6, a=3, b=4)
test('hello', key='world')