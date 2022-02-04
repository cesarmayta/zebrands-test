from django.urls import path

from . import views

urlpatterns = [
    path('',views.indexView.as_view()),
    path('product',views.ProductView.as_view()),
    path('product/<int:product_id>',views.ProductDetailView.as_view())
]