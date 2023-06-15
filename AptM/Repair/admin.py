from django.contrib import admin
from Repair.models import TypeRepair
from Repair.models import Repair
# registration your models here.


class TypeRepairCreate(admin.ModelAdmin):
    pass


class Repairs(admin.ModelAdmin):
    pass


admin.site.register(Repair, Repairs)
admin.site.register(TypeRepair, TypeRepairCreate)