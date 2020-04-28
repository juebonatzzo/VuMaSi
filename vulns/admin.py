from django.contrib import admin
from .models import Vulnerability,CVE
import csv
from django.http import HttpResponse

admin.site.register(CVE)


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class CVEInline(admin.TabularInline):
    model = CVE


@admin.register(Vulnerability)
class HeroAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['name','state','cves_display','modified_date']
    list_filter = ['state','creation_date','impact']
    search_fields = ['name','description','solution','cves__cve_id']
    inlines = [CVEInline]
    actions = ["export_as_csv","send_mail"]

    def cves_display(self, obj):
        return ", ".join([
            child.cve_id for child in obj.cves.all()
        ])
    cves_display.short_description = "CVEs"

    def send_mail(self, request, queryset):
        pass

    send_mail.short_description = "Send Email Selected"

    # list_editable = ['state']
    # date_hierarchy = 'creation_date'
