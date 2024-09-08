from django.contrib import admin
from .models import Post,Category,Comment
from django_summernote.admin import SummernoteModelAdmin
class ContactAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('author','title','login_required', 'count_view', 'status', 'publish_date', 'created_at')
    list_filter = ('status','author')
    summernote_fields = ('content',)
    search_fields = ['title', 'content','author']

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = '-empty-'
    list_display = ('post', 'name', 'email', 'subject','message','approved', 'created_at','updated_at')
    list_filter = ('approved', 'name')
    search_fields = ['name', 'email']

admin.site.register(Post,ContactAdmin)
admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
