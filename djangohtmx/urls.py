from django.contrib import admin
from django.urls import path

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('<int:pk>/', views.author_detail, name='author-detail'),
    path('htmx/book/<int:pk>/detail/', views.detail_book, name='detail-book'),
    path('htmx/book/create/', views.create_book_form, name='create-book'),
    path('htmx/book/<int:pk>/delete/', views.delete_book, name='delete-book'),
    path('htmx/book/<int:pk>/update/', views.update_book_form, name='update-book'),
]
