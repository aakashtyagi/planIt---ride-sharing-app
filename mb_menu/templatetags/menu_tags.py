from django import template
from django.core.urlresolvers import reverse, reverse_lazy
from django.template import Node
from mb_menu.models import MenuItem, FooterLink
register = template.Library()

@register.tag
def get_menu_items(parser, token):
    args = token.split_contents()
    items = MenuItem.objects.filter(item_active=True, item_parent=0).order_by('item_sort_order', 'item_name')
    return MenuItemNode(items)


class MenuItemNode(Node):

    def __init__(self, menu_items):
        self.items = menu_items

    def render(self, context):
        html = ""
        for item in self.items:
            subitems = MenuItem.objects.filter(item_active=True, item_parent=item.id).order_by('item_sort_order', 'item_name')
            if subitems:
                html += "<li class='dropdown'><a href='#' class='dropdown-toggle' data-toggle='dropdown'>%s&nbsp;<b class='caret'></b></a><ul class='dropdown-menu'>" % item.item_name
                for subitem in subitems:
                    split = subitem.item_link.split(' ')
                    html += "<li><a href='%s'>%s</a></li>" % (reverse(subitem.item_link, kwargs={'slug': subitem.item_slug}), subitem.item_name)
                html += "</ul></li>"
            else:
                url = reverse(item.item_link)
                request = context['request']
                css = '%s %s %s %s %s' % ('visible-xs' if item.item_visible_xs else 'hidden-xs',
                'visible-sm' if item.item_visible_sm else 'hidden-sm',
                'visible-md' if item.item_visible_md else 'hidden-md',
                'visible-lg' if item.item_visible_lg else 'hidden-lg',
                'active' if request.path == url else '')
                icon = ''
                if item.item_requires_login:
                    if request.user.is_authenticated() == False:
                        continue
                if item.item_requires_anon:
                    if request.user.is_authenticated() == True:
                        continue
                if len(item.item_glyph):
                    icon = '<span class="glyphicon %s"></span>' % item.item_glyph
                html += '<li class="%s"><a href="%s">%s%s</a></li>' % (css, url, icon, item.item_name)
        return html


@register.tag
def get_footer_links(parser, token):
    args = token.split_contents()
    items = FooterLink.objects.filter(item_active=True).order_by('item_sort_order', 'item_name')
    return FooterLinkNode(items)


class FooterLinkNode(Node):

    def __init__(self, menu_items):
        self.items = menu_items

    def render(self, context):
        html = "<div class='footer-links'>"
        items = list()
        request = context['request']
        for item in self.items:
            if item.item_requires_login:
                if request.user.is_authenticated() == False:
                    continue
            if item.item_requires_anon:
                if request.user.is_authenticated() == True:
                    continue
            items.append(item)

        for id, item in enumerate(items):
            url = reverse(item.item_link)
            css = '%s%s%s%s' % ('' if item.item_visible_xs else ' hidden-xs',
                '' if item.item_visible_sm else ' hidden-sm',
                '' if item.item_visible_md else ' hidden-md',
                '' if item.item_visible_lg else ' hidden-lg',)

            html += "<span class='footer-link%s'><a class='btn-link' href='%s'>%s</a></span>" % (css, url, item.item_name)
            #html += "</span>"
            if id is not len(items) - 1:
                html += "<span class='footer-seperator'>|</span>"
        html += "</div>"
        return html


