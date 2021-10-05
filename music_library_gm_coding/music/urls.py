from django.urls import path
from music import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:pk>/', views.SongDetail.as_view()),
]