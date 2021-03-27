from django.contrib import admin

from .models import UserStory, UserPage, ReaderStory, ReaderPage

class PageInline(admin.TabularInline):
    model = UserPage
    extra = 3


class UserStoryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['story_text', 'story_img', 'slug', 'is_ad', 'ad_cta', 'ad_url', 'up_next_title', 'up_next_img', 'up_next_url']}) ]
    inlines = [PageInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(UserStory, UserStoryAdmin)

class PageInline(admin.TabularInline):
    model = ReaderPage
    extra = 3


class ReaderStoryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['story_text', 'story_img', 'slug', 'is_ad', 'ad_cta', 'ad_url', 'up_next_title', 'up_next_img', 'up_next_url']}) ]
    inlines = [PageInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(ReaderStory, ReaderStoryAdmin)