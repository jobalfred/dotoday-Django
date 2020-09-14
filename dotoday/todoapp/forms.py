from django import forms
from django.forms import ModelForm
from .models import TaskToDo


class ToDoFroms(forms.ModelForm):
    class Meta:
        model = TaskToDo
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ToDoFroms,self).__init__(*args, **kwargs)
