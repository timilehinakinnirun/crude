from django.contrib import admin

from .models import Artiste, Lyrics, Song

# Register your models here.

admin.site.register(Artiste)
admin.site.register(Song)
admin.site.register(Lyrics)