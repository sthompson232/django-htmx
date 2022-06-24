from django.contrib import admin
from django.urls import path

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<pk>/', views.create_book, name='create-book'),
    path('htmx/book/<pk>/detail/', views.detail_book, name='detail-book'),
    path('html/book/create/', views.create_book_form, name='create-book'),
    path('htmx/book/<pk>/delete/', views.delete_book, name='delete-book'),
    path('htmx/book/<pk>/update/', views.update_book_form, name='update-book'),
]
