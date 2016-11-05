from mb_database import fields as f
from mb_database import models as m

class MenuItem(m.Model):
    item_name = f.CharField(max_length=50, default=None, null=True, blank=False)
    item_link = f.CharField(max_length=150, default=None, null=True, blank=False)
    item_created = f.DateTimeField(default=None, null=True, blank=True, auto_now_add=True)
    item_active = f.BooleanField(default=False, blank=True)
    item_sort_order = f.IntegerField(default=0, null=True, blank=True)
    item_parent = f.IntegerField(default=0, null=True, blank=True)
    item_slug = f.CharField(max_length=20, default=None, null=True, blank=True)
    item_requires_login = f.BooleanField(default=False, blank=True)
    item_requires_anon = f.BooleanField(default=False, blank=True)
    item_glyph = f.CharField(max_length=100, default=None, null=True, blank=True)
    item_visible_lg = f.BooleanField(default=True, blank=True)
    item_visible_md = f.BooleanField(default=True, blank=True)
    item_visible_sm = f.BooleanField(default=True, blank=True)
    item_visible_xs = f.BooleanField(default=True, blank=True)

    class Meta:
        db_table = "MB_MENU_ITEM"
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"

    def __unicode__(self):
        return self.item_name


class FooterLink(m.DataModel):
    item_name = f.CharField(max_length=50, default=None, null=True, blank=False)
    item_link = f.CharField(max_length=150, default=None, null=True, blank=False)
    item_created = f.DateTimeField(default=None, null=True, blank=True, auto_now_add=True)
    item_active = f.BooleanField(default=False, blank=True)
    item_sort_order = f.IntegerField(default=0, null=True, blank=True, unique=True)
    item_requires_login = f.BooleanField(default=False, blank=True)
    item_requires_anon = f.BooleanField(default=False, blank=True)
    item_visible_lg = f.BooleanField(default=True, blank=True)
    item_visible_md = f.BooleanField(default=True, blank=True)
    item_visible_sm = f.BooleanField(default=True, blank=True)
    item_visible_xs = f.BooleanField(default=True, blank=True)

    class Meta:
        db_table = "MB_FOOTER_LINK"
        verbose_name = "Footer Link"
        verbose_name_plural = "Footer Links"
