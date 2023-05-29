from django.urls import path 
from base.views import product_views as views

urlpatterns = [
    path('', views.getProducts, name='products'),
    path('top/', views.getTopProducts, name='top-product'),
    path('create/', views.createProduct, name='create'),
    path('upload/', views.uploadImage, name='upload-image'),
    path('<str:pk>/', views.getProduct, name='product'),
    path('<str:pk>/reviews/', views.createProductReview, name='product'),
    
    
    path('update/<str:pk>/', views.updateProduct, name='update'),
    path('delete/<str:pk>/', views.deleteProducts, name='delete'),
]
