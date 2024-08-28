from django.contrib import admin
from . models import UserAccount
from unfold.admin import ModelAdmin
from django.utils.html import format_html





class UserAdmin(ModelAdmin):
	list_display = ['id', 'image_tag' ,'username', 'email']

	def image_tag(self, obj):
		return format_html('<img src="{}" width=100 height=100 border=1/>'.format(obj.picture.url))
	
	image_tag.short_description = "Image"

admin.site.register(UserAccount, UserAdmin)


