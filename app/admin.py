from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(Hobbies)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(DisLike)
