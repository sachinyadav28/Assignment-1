from django.contrib import admin
from user_profile.models import UserProfile, ProfileFeed
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ProfileFeed)