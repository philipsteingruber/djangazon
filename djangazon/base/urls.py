from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<str:pk>', views.view_item, name='view-item'),
    path('buy/<str:pk>/', views.buy_item, name='buy-item'),
    path('signout/', views.sign_out, name='sign-out'),
    path('item/<str:pk>/delete/<str:amount>', views.delete_item_from_cart, name='delete-item-from-cart'),
    path('profile/<str:pk>', views.user_profile, name='user-profile'),
    path('login/', views.login_user, name='login'),
]
