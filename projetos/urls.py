from django.contrib import admin
from django.urls import include, path
from projetos import views


urlpatterns = [
    path('', views.view_all_projects),
    path('<int:pk>', views.project_detail),
]
