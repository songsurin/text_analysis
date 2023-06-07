from django.contrib import admin
from django.urls import path
from travel import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.recommend),
    path('query', views.query),
    path('delete_chat', views.delete_chat),
    path('result', views.recommend),
    path('research1', views.research1),
]
