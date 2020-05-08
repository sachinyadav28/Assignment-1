from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from library_management.models import Books, Author

def make_available(modeladmin, request, queryset):
    queryset.update(available=True)
make_available.short_description = "Mark as available"

def make_unavailable(modeladmin, request, queryset):
    queryset.update(available=False)
make_unavailable.short_description = "Mark as unavailable"

class BookssAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'title', 'author', 'genere', 'available']
    actions = [make_available, make_unavailable]

class UserAdminSite(AdminSite):
    pass

user_admin_site = UserAdminSite(name='user-admin')

admin.site.register(Books,BookssAdmin)
admin.site.register(Author)
admin.site.site_header ='Library Management Portal'
admin.site.index_title = 'Library'
admin.site.unregister(Group)
admin.site.unregister(User)
user_admin_site.register(User)
user_admin_site.register(Group)
