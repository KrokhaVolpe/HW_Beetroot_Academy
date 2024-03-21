from django.shortcuts import render
from .models import Notes, Category


def index(request):
    categories = get_categories()
    notes = get_notes()
    return render(request, 'index.html', {'categories': categories, 'notes': notes})


def get_categories():
    categories = Category.objects.order_by('date_added')
    return categories

def get_notes():
    notes = Notes.objects.all()
    return notes
    

    

