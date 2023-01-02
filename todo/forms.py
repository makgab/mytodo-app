from django import forms

from .models import Todo
from .models import Type


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('todo','description', 'type',)

class TypeForm(forms.ModelForm):

    class Meta:
        model = Type
        fields = ('type',)

