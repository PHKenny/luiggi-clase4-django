import re
from typing import Self

import layrz_forms as forms


class LoginForm(forms.Form):
  username = forms.CharField(max_length=150, min_length=3, required=True)
  password = forms.CharField(max_length=128, min_length=6, required=True)

  def clean_username(self: Self) -> None:
    username = self.cleaned_data.get('username')
    if not username:
      return

    username_rgx = re.compile(r'^[^\s]+$')
    if not username_rgx.match(username):
      self.add_errors(key='username', code='invalid')
      return


class SessionForm(forms.Form):
  def clean_token(self: Self) -> None:
    token = self.cleaned_data.get('token')
    if not token:
      self.add_errors(key='token', code='required')
      return

    token_rgx = re.compile(r'^[a-zA-Z0-9]{128}$')
    if not token_rgx.match(token):
      self.add_errors(key='token', code='invalid')
      return
