from django.urls import path
from . import views


urlpatterns = [
    path('cart/', views.CartList.as_view()),
    path('cart/<int:pk>/', views.CartDetail.as_view()),
    path('cartproduct/', views.CartProductList.as_view()),
    path('cartproduct/<int:pk>/', views.CartProductDetail.as_view()),
]