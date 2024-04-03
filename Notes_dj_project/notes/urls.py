from django.urls import path
from django.contrib.auth import views as auth_views
from .  import views


urlpatterns = [
    path('register/', views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('new_notes/<int:category_id>/', views.new_notes, name='new_notes'),
    path('new_category', views.new_category, name='new_category'),
    path('categories/<int:category_id>/', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.categories, name='categories'),
    path('note/<int:note_id>/delete/', views.delete_note, name='delete_note'),
    path('category/<int:category_id>/delete/', views.delete_category, name='delete_category'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('search/', views.search_notes, name='search_notes'),
    path('', views.index, name='index'),
 
]
