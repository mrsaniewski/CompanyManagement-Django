from django.contrib import admin
from .models import User, Item, Prize

# Register your models here.
admin.site.register(User)
admin.site.register(Item)
admin.site.register(Prize)
