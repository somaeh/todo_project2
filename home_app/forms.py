from django import forms

from.models import Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())
    created = forms.DateField()
    
class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body')