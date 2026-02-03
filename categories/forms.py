import layrz_forms as forms

from categories.enums import CategoryType


class CategoryForm(forms.Form):
  name = forms.CharField(max_length=255, min_length=3, required=True)
  description = forms.CharField(max_length=1024, required=False)
  kind = forms.CharField(choices=CategoryType.choices, required=True)  # type: ignore
