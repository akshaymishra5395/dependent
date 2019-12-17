from django.contrib import admin
from .models import Building,BuidingAccessRole
from .forms import BuildAccessRoleAdminForm

class BuildingAccessRoleAdmin(admin.ModelAdmin):
    form = BuildAccessRoleAdminForm
    class Media:
        js = ("takelog/admin/js//my_code.js",)

admin.site.register(Building)
admin.site.register(BuidingAccessRole ,BuildingAccessRoleAdmin)
# Register your models here.
