from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path('contact', views.contact, name = 'contact us'),
    path('about', views.about, name = 'about'),
    path('tracker', views.tracker, name = 'tracking status'),
    path('productview', views.productview, name = 'product view'), 
    path('search', views.search, name = 'search product'),
    path('checkout', views.checkout, name = 'checkout'),

]