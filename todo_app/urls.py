from django.urls import path
from .views import TodoListView, TodoitemDetailView

urlpatterns = [
    path('', TodoListView.as_view()),
    path('<int:pk>/',TodoitemDetailView.as_view()),

]