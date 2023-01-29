from django import forms
from .models import *


class SelectFoodForm(forms.ModelForm):
    class Meta:
        model = SelectFoodItem
        fields = "__all__"

    def __init__(self, user, *args, **kwargs):
        super(SelectFoodForm, self).__init__(*args, **kwargs)
        self.fields['name'].queryset = FoodItem.objects.filter(person=user)
