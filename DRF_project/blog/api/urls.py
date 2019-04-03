from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.PostListAPIView.as_view()),
    path('<int:pk>/', views.PostDetailAPIView.as_view()),
    path('update/<int:pk>/', views.PostUpdateAPIView.as_view()),
    path('delete/<int:pk>/', views.PostDeleteAPIView.as_view()),
    path('create/', views.PostCreateAPIView.as_view()),
]