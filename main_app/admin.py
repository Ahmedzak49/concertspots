from django.contrib import admin
from .models import Ticket, Concert

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Concert)
