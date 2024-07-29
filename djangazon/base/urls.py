from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<str:pk>', views.view_item, name='item'),
]
