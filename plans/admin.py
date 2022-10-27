from django.contrib import admin
from .models import Class, Week, Plan

# regristiert das Klassen-Model zum Admin-Pannel
admin.site.register(Class)
# regristiert das Wochen-Model zum Admin-Pannel
admin.site.register(Week)
# regristiert das Blockpläne-Model zum Admin-Pannel
admin.site.register(Plan)
