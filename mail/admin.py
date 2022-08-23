from django.contrib import admin

# Register your models here.
from mail.models import MailInfo

admin.site.site_header = 'Mail Admin'
admin.site.site_title = 'Mail Admin'
admin.site.index_title = 'Mail Admin'


@admin.register(MailInfo)
class MainInfoAdmin(admin.ModelAdmin):
    pass
