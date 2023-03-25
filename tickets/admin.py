from django.contrib import admin
from .models import Guest, Reservation, Movie, post

admin.site.register(Guest)
admin.site.register(Reservation)
admin.site.register(Movie)
admin.site.register(post)
# Register your models here.
