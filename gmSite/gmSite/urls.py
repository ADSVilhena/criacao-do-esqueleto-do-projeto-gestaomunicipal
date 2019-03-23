from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cadastros/', include('cadastros.urls')),
    path('admin/', admin.site.urls),
]