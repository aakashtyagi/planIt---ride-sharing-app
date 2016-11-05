from django.contrib import admin
from models import MenuItem, FooterLink

class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'item_link', 'item_sort_order', 'item_active']
    exclude = ['item_created']

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'item_sort_order', 'item_parent', 'item_slug', 'item_active']
    exclude = ['item_created']

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(FooterLink, FooterLinkAdmin)