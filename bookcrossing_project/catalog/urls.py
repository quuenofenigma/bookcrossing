from django.urls import path

from . import views

app_name = 'catalog'


urlpatterns = [
    path('', views.index_views, name='index_views'),
    path('book/<int:id>/', views.book_views, name='book_views'),
    path('categories/', views.categories_views, name='categories_views'),
    path('category/<str:category_str>/', views.category_views,
         name='category_views'),
]
