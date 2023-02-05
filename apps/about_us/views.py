from rest_framework.viewsets import ModelViewSet

from apps.about_us.models import Video, WhatsApp, Main
from apps.about_us.serializers import VideoSerializer, WhatsAppSerializer, \
    MainSerializer


class VideoView(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class WhatsAppView(ModelViewSet):
    queryset = WhatsApp.objects.all()
    serializer_class = WhatsAppSerializer


class MainView(ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
