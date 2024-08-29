from django.contrib import admin
from . models import Post, Category, Tag
from unfold.admin import ModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget, ArrayWidget
from django.utils.html import format_html
from django.db import models




# class MyInline(TabularInline):
#     model = Post
#     tab = True


class PostAdmin(ModelAdmin):
    list_display = ['id','image_tag','title', 'category', 'status', 'published_on', 'updated_on']
    list_display_links = ['title', 'image_tag']
    list_filter = ["author"]
    list_filter_submit = True
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        # ArrayField: {
        #     "widget": ArrayWidget,
        # }
    }

    def image_tag(self, obj):
        return format_html('<img src="{}" width=100, height=100 /> '.format(obj.get_image_url))
    
    image_tag.short_description = "Image"




class TagAdmin(ModelAdmin):
    list_filter_submit = True
    list_display = ['id','name']
    list_display_links = ['id','name']


class CategoryAdmin(ModelAdmin):
    list_filter_submit = True
    list_display = ['id','name']
    list_display_links = ['id', 'name']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
