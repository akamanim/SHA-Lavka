from django.urls import path
from . import views


urlpatterns = [
    path('product/all/list/', views.ProductList.as_view()),
    path('category/all/list/', views.CategoryList.as_view()),
    path('product_detail/<int:pk>/', views.ProductDetail.as_view()),
]

