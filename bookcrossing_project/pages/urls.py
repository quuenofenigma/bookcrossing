from django.urls import path

from .views import StaticPageAbout

app_name = 'pages'

urlpatterns = [
    path('about/', StaticPageAbout.as_view(), name='about_views'),
]