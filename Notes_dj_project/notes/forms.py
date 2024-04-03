from django import forms
from .models import Category, Notes


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        labels = {'title': 'Заголовок'}
        

class NotesForm(forms.ModelForm):
    
    class Meta:
        model = Notes
        fields = ['title', 'text']
        labels = {'title': 'Заголовок', 'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class NoteSearchForm(forms.Form):
    title = forms.CharField(label='Заголовок', max_length=100, required=False)


    
