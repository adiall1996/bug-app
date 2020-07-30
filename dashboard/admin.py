from django.contrib import admin
from .models import Developer,BugTracker,Assign_developer
# Register your models here.

admin.site.register(Developer)
admin.site.register(BugTracker)
admin.site.register(Assign_developer)