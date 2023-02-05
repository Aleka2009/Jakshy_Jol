from django.contrib import admin

from apps.about_us.models import Main, WhatsApp, Video

admin.site.register(Video)
admin.site.register(WhatsApp)
admin.site.register(Main)
