from django.urls import path
from .views import HomeView, AboutView, PortfolioView

app_name = 'portfolio'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
    # Add more URL patterns as needed
]
