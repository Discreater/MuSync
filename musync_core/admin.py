from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(Album)