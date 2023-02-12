from django.contrib import admin
from django.urls import path
from brand import views as brand_view

urlpatterns = [
     path('create_brand_name', brand_view.create_brand_name,name = 'create_brand_name'),
     path('view_brand_name/<int:brand_id>', brand_view.view_brand_name,name = 'view_brand_name'),
     path('home_page/<int:brand_id>', brand_view.homepage_fn, name = 'home_page'),
]
