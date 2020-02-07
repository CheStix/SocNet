from django.urls import path

from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.image_create, name='create_url'),
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
]
