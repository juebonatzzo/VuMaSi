from django.contrib import admin
from .models import Vulnerability,CVE
# Register your models here.

admin.site.register(CVE)


class CVEInline(admin.TabularInline):
    model = CVE


@admin.register(Vulnerability)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['name','state','cves_display']
    list_filter = ['state']
    inlines = [CVEInline]

    def cves_display(self, obj):
        return ", ".join([
            child.cve_id for child in obj.cves.all()
        ])
    cves_display.short_description = "CVEs"