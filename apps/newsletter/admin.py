from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Newletter, Subscriber
from unfold.widgets import UnfoldAdminTextareaWidget
# from django.contrib.postgres.fields import ArrayField
from django.db import models
from unfold.contrib.forms.widgets import WysiwygWidget, ArrayWidget





# FORMFIELD_OVERRIDES = {
#     models.TextField: {"widget": WysiwygWidget},
# }



class SubscriberAdmin(ModelAdmin):
    list_filter = ['confirmed', 'conf_num']
    list_display = ['id', 'email', 'conf_num', 'confirmed']
    list_display_links = ['id', 'email']




class NewsletterAdmin(ModelAdmin):
    list_display = ['id', 'author', 'subject', 'status', 'written_on', 'last_modified']
    list_display_links = ['id', 'subject']
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
        # ArrayField: {
        #     "widget": ArrayWidget,
        # }
    }


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Newletter, NewsletterAdmin)

