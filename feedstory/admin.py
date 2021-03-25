from django.contrib import admin

from .models import Story, Page

admin.site.site_header = "Modern Trends Admin"
admin.site.site_title = "Modern Trends Admin Area"
admin.site.index_title = "Welcome to the Modern Trends admin area"


class PageInline(admin.TabularInline):
    model = Page
    extra = 3


class StoryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['story_text', 'story_img', 'slug', 'is_ad', 'ad_cta', 'ad_url']}) ]
    inlines = [PageInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Story, StoryAdmin)