from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse
from .models import Notes, Category
from .forms import CategoryForm, NotesForm, NoteSearchForm


def index(request):
    return render(request, 'index.html')


@login_required
def categories(request):
    categories = Category.objects.filter(owner=request.user).order_by('date_added')
    context = {'categories': categories}
    return render(request, 'categories.html', context)


@login_required
def category(request, category_id):
    category = Category.objects.get(id=category_id)
    if category.owner != request.user:
        raise Http404
    notes = Notes.objects.filter(category=category).order_by('-reminder')
    context = {'category': category, 'notes': notes}
    return render(request, 'category.html', context)


@login_required
def new_category(request):
    if request.method != 'POST':
        form = CategoryForm()
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.owner = request.user
            new_category.save()
            return redirect('categories')

    context = {'form': form}
    return render(request, 'new_category.html', context)


@login_required
def new_notes(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method != 'POST':
        form = NotesForm()
    else:
        form = NotesForm(data=request.POST)
        if form.is_valid():
            new_notes = form.save(commit=False)
            new_notes.category = category
            new_notes.save()
            return redirect('category', category_id=category_id)


    context = {'category': category, 'form': form}
    return render(request, 'new_notes.html', context)


@login_required
def edit_note(request, note_id):
    note = Notes.objects.get(id=note_id)
    category = note.category
    if category.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('category', category_id=category.id)
    else:
        form = NotesForm(instance=note)

    context = {'note': note, 'category': category, 'form': form}
    return render(request, 'edit_note.html', context)


@login_required
def delete_category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return redirect('categories')

    if category.owner != request.user:
        messages.error(request, "Ви не маєте дозволу на видалення цієї категорії.")
        return redirect('categories')

    Notes.objects.filter(category=category).delete()

    category.delete()

    messages.success(request, "Категорію та всі пов'язані з нею нотатки успішно видалено.")
    return redirect('categories')


@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)

    if note.category.owner != request.user:
        messages.error(request, "Ви не маєте дозволу на видалення цієї нотатки.")
        return redirect('categories')

    if request.method == 'POST':
        note.delete()
        messages.success(request, "Нотатку успішно видалено.")
        return redirect('category', category_id=note.category.id)

    return render(request, 'delete_note.html', {'note': note})


def search_notes(request):
    if request.method == 'GET':
        form = NoteSearchForm(request.GET)
        notes = Notes.objects.all()

        if form.is_valid():
            title = form.cleaned_data.get('title')
            if title:
                notes = notes.filter(title__icontains=title)
            else:
                return HttpResponse("Поле пошуку не може бути порожнім")

        context = {'form': form, 'notes': notes}
        return render(request, 'search_notes.html', context)
    else:
        return HttpResponse("Метод HTTP не підтримується")


def register(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            try:
                new_user = form.save()
            except Exception as e:
                print(f"Помилка: {e}")
            login(request, new_user)
            return redirect('index')

    context = {'form': form}
    return render(request, 'register.html', context)
