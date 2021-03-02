from django.urls import path
from .views import HomePageView, AboutPageView, ContentPageView

urlpatterns = [
    path('',HomePageView.as_view(), name='Home'),
    path('About',AboutPageView.as_view(), name='About'),
    path('content',ContentPageView.as_view(), name='content'),
]
