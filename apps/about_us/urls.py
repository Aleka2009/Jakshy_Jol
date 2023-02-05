
from django.urls import path

from apps.about_us.views import VideoView, WhatsAppView, MainView

urlpatterns = [
    path('video/', VideoView.as_view({'get': 'list'})),
    path('whatssapp/', WhatsAppView.as_view({'get': 'list'})),
    path('main/', MainView.as_view({'get': 'list'})),
]
