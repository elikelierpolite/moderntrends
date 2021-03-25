from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Article, Discover, DiscoverPage, Topten, ListItem, Celebrity, Weview, Video, Finance, Future, Product, Productotd

class PageInline(admin.TabularInline):
    model = DiscoverPage
    extra = 3


class DiscoverAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title','discover_text', 'discover_img', 'hook', 'slug', 'is_ad', 'cta', 'url']}) ]
    inlines = [PageInline]
    
class ListInline(admin.TabularInline):
    model = ListItem
    extra = 10


class ToptenAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title', 'list_headline', 'list_img', 'slug']}) ]
    inlines = [ListInline]

admin.site.register(Article)
admin.site.register(Discover, DiscoverAdmin)
admin.site.register(Topten, ToptenAdmin)
admin.site.register(Celebrity)
admin.site.register(Weview)
admin.site.register(Video)
admin.site.register(Finance)
admin.site.register(Future)
admin.site.register(Product)
admin.site.register(Productotd)

