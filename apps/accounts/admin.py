from django.contrib import admin
from . models import UserAccount
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from django.contrib.auth.models import Group




class UserAdmin(ModelAdmin):
	list_display = ['id', 'image_tag' ,'username', 'email']
	list_display_links = ['image_tag', 'email', 'username']

	def image_tag(self, obj):
		return format_html('<img src="{}" width=80 height=60 style="border-radius: 50px;"/>'.format(obj.picture.url)) if obj.picture else ""
	
	image_tag.short_description = "Image"

admin.site.register(UserAccount, UserAdmin)


admin.site.unregister(Group)

class GroupAdmin(ModelAdmin):
	pass 

admin.site.register(Group, GroupAdmin)

