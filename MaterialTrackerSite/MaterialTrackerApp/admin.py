from django.contrib import admin
from MaterialTrackerApp.models import *
 

# Register your models here.
admin.site.register(Project)
admin.site.register(Item)
admin.site.register(Transaction)
admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(Currency)