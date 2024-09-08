from django.contrib import admin
from .models import Contact,NewsLetter
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ('name', 'email', 'subject', 'message','created_at','updated_at')
admin.site.register(Contact,ContactAdmin)
admin.site.register(NewsLetter)



