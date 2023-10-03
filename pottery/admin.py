from django.contrib import admin
from .models import  Industry, Area, Report

class IndustryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("technique",)
    ordering = ('name',)

admin.site.register(Industry, IndustryAdmin)

class AreaAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("region",)
    ordering = ('name',)

admin.site.register(Area, AreaAdmin)

class ReportAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    ordering = ('name',)

admin.site.register(Report, ReportAdmin)