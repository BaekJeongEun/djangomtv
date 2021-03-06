from django.contrib import admin
from .models import Notice
# Register your models here.

#admin.site.register(Notice)

@admin.register(Notice) # 데코레이터
class NoticeAdmin(admin.ModelAdmin):
    list_display = ['title', 'likeCount']
    list_display_links = ['title', 'likeCount']