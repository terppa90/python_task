from django.urls import path

from webshop_api import views

urlpatterns = [
    # path("home/", views.ProductApiView.as_view()),
    #path("home/", views.AllProductsView.as_view()),
    path("products/", views.allProducts),
    path("products/<int:pk>", views.product_detail),
    # path('hello-view/', views.HelloApiView.as_view()),
    #path('products-view/', views.ProductApiView.as_view()),
]
