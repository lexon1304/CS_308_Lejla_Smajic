from django.urls import path
from Books import views

urlpatterns = [
    path('Books/', views.books_list.as_view()),
    path('Books/<int:pk>/', views.books_detail.as_view()),
]

