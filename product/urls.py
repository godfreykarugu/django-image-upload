from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name='home'),
    path('insert_product/', views.insert_product, name='insert-product'),
    path('display_products/', views.display_products, name='display-products'),
    path('product_details/<id>', views.product_details, name='product-details'),
    path('update_product/<id>', views.update_product, name='update-product'),
    path('delete_product/<id>', views.delete_product, name='delete-product'),
    path('add_student/', views.add_student, name='add-student'),
    path('view_details/<id>',views.view_details,name="view-details")
]
