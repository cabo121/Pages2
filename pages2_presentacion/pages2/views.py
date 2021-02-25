from django.views.generic.base import TemplateView

class HomePageView (TemplateView):
    template_name = 'Home.html'

class AboutPageView (TemplateView):
    template_name = 'About.html'
    
