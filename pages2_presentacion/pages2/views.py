from django.views.generic.base import TemplateView

class HomePageView (TemplateView):
    template_name = 'Home.html'

class AboutPageView (TemplateView):
    template_name = 'About.html'

class ContentPageView (TemplateView):
    template_name = 'content.html'
    
