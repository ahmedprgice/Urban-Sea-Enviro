from django.contrib import admin
from django.urls import path
from USeCleaning.views import USeCleaning, booking_page, home, about
from USENutrition.views import useNutrition


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('USeCleaning/', USeCleaning, name='USeCleaning'),
    path('about/', about, name='about'),
    path('book/', booking_page, name='booking'),   # <-- NEW ROUTE
     path('USeNutrition/', useNutrition, name='USeNutrition'),
]
