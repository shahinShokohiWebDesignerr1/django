
from django.urls import include, path
from .views import HomeView,AboutView,ContactView
urlpatterns = [
    path('', HomeView.as_view()),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view())
]
