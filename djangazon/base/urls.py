from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<str:pk>', views.view_item, name='view-item'),
    path('buy/<str:pk>/', views.buy_item, name='buy-item'),
    path('signout/', views.sign_out, name='sign-out'),
]
