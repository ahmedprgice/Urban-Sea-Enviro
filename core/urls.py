from django.contrib import admin
from django.urls import path
from USeCleaning.views import USeCleaning, booking_page, home, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('USeCleaning/', USeCleaning, name='USeCleaning'),
        path('about/', about, name='about'),
    path('book/', booking_page, name='booking'),   # <-- NEW ROUTE
]
