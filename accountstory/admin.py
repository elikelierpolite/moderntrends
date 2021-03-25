from django.contrib import admin

from .models import AccountStory, AccountPage

class PageInline(admin.TabularInline):
    model = AccountPage
    extra = 3


class AccountStoryAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['story_text', 'story_img', 'slug', 'is_ad', 'ad_cta', 'ad_url']}) ]
    inlines = [PageInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(AccountStory, AccountStoryAdmin)