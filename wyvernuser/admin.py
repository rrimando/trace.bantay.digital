from django.contrib import admin

# Register your models here.
# the module name is app_name.models
from wyvernuser.models import User

class UserAdmin(admin.ModelAdmin):
    search_fields = ('email', 'first_name', 'last_name', 'address' )

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(User, UserAdmin)

