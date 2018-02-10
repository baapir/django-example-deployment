from django.contrib import admin
from .models import Topic, Webpage, AccessRecord, UserAdded

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(UserAdded)