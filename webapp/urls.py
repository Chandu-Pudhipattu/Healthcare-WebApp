from . import views
from django.urls import path

urlpatterns = [
   path('',views.home,name='home'),
   path('home/',views.home,name='home'),
   path('heart/',views.heart,name='heart'),
   path('parkinsons/',views.parkinsons,name='parkinsons'),
   path('insurance/',views.insurance,name='insurance')
]
