from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Pdd import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('apps.about_us.urls')),
    # path('test_pdd/', include('apps.test_pdd.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
