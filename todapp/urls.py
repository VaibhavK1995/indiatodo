from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="list"),
	path('startodo', views.start, name='startodo'),
	path('update_task/<str:pk>/', views.updateTask, name='update'),
	path('delete_task/<str:pk>/', views.deleteTask, name='delete'),
]
