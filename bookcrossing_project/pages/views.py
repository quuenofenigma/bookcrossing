from django.views.generic.base import TemplateView


class StaticPageAbout(TemplateView):
    template_name = 'pages/about.html'
