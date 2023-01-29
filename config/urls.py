from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('calorietracker.urls')),
    path('admin/', admin.site.urls),
    path('manage/', include('calorietracker.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('accounts.urls'))
]
