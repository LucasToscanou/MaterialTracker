from django.contrib import admin
from MaterialTrackerApp.models import *
 

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectUser)
admin.site.register(Material)
admin.site.register(MaterialTransaction)
admin.site.register(UserProfile)
admin.site.register(Location)
admin.site.register(Currency)