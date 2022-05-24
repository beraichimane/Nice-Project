from django.contrib import admin
from .models import Event ,EventLink,EventLocalisation

admin.site.register(Event)
admin.site.register(EventLink)
admin.site.register(EventLocalisation)
# Register your models here.
