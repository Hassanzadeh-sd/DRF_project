"""DRF_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('blog.api.urls',namespace='post-api')),
    path('api-token-auth/', obtain_jwt_token),
]


"""
curl -X POST -d "username=hassanzadeh&password=123qwe!@#" http://127.0.0.1:8000/api-token-auth/


curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imhhc3NhbnphZGVoIiwiZXhwIjoxNTU0NDY0MDkxLCJlbWFpbCI6IiJ9.YZeTblaVC3_SY19V9ZzIQU3GFrdm8PBya-0b67YX3K8" http://127.0.0.1:8000/api/posts/

"""