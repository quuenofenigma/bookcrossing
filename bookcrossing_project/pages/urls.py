from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'pages'

urlpatterns = [
    path('about/', TemplateView.as_view(template_name='pages/about.html'),
         name='about'),
]
