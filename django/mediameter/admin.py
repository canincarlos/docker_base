from django.contrib import admin

from .models import Tweeter, Tweet, ParentGroup
# Register your models here.

admin.site.register(ParentGroup)
admin.site.register(Tweeter)
admin.site.register(Tweet)