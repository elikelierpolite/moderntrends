from django.contrib import admin

from .models import BlogStory, BlogPage

class PageInline(admin.TabularInline):
    model = BlogPage
    extra = 3


class BlogStoryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['story_text', 'story_img', 'slug', 'is_ad', 'ad_cta', 'ad_url', 'up_next_title', 'up_next_img', 'up_next_url']}) ]
    inlines = [PageInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(BlogStory, BlogStoryAdmin)