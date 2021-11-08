from django.contrib import admin

from profiles_api import models

# This makes the admin user accessible form the admin interface
admin.site.register(models.UserProfile)