from django.urls import path, re_path
from . import views

app_name="blog"

urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='list'),
    path('<int:pk>/', views.PostDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', views.PostUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PostDeleteAPIView.as_view(), name='delete'),
    path('create/', views.PostCreateAPIView.as_view(), name='detail'),
]