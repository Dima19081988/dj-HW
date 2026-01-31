from django.urls import path
from . import views

urlpatterns = [
	path('', views.books_view, name='books_list'),
	path('<pub_date>/', views.books_by_date, name='books_by_date')
]