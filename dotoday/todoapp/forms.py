from django import forms
from django.forms import ModelForm
from .models import TaskToDo


class ToDoFroms(forms.ModelForm):
    taskName = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add your Text'}))
    class Meta:
        model = TaskToDo
        fields = ('taskName',)

    def __init__(self, *args, **kwargs):
        super(ToDoFroms,self).__init__(*args, **kwargs)
        self.fields['taskName'].widget.attrs['style'] = 'width:400px; height:40px;'
