from django.urls import path
from .views import LogoutViews,LoginViews,SingupViews
app_name = 'Accounts'
urlpatterns = [
    path('login/',LoginViews.as_view(),name='login'),
    path('logout/',LogoutViews.as_view(),name='logout'),
    path('sinup/',SingupViews.as_view(),name='sinup'),
    ]