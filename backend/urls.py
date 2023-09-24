from django.contrib import admin
from django.urls import path
from News import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/add_news', views.add_news),
    path('api/news', views.get_news)
]