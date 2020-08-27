from django.contrib import admin

# Register your models here.
# the module name is app_name.models
from wyverntrace.models import WyvernTraceLog
from wyverntrace.models import WyvernMedicalForm

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.
admin.site.register(WyvernTraceLog)
admin.site.register(WyvernMedicalForm)
