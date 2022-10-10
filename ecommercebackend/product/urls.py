from django.urls import path
from . import views
urlpatterns = [
    path('category/', views.CategoryList.as_view()),
    path('category/<int:pk>/', views.CategoryDetail.as_view()),
    path('subcategory/', views.SubCategoryList.as_view()),
    path('subcategory/<int:pk>/', views.SubCategoryDetail.as_view()),
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('productreview/', views.ProductReviewList.as_view()),
    path('productreview/<int:pk>/', views.ProductReviewDetail.as_view()),
]
