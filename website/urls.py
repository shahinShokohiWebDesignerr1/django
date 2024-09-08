
from django.urls import path
from .views import HomeView,AboutView,ContactView,NewsLetterView
app_name = 'website'


urlpatterns = [
    path('', HomeView.as_view(),name = 'home'),
    path('about/', AboutView.as_view(),name = 'about'),
    path('contact/', ContactView.as_view(),name = 'contact'),
    path('newsletter/', NewsLetterView.as_view(),name = 'news-letter'),

]
