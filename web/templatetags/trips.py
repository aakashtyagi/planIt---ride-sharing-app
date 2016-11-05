from django.template import Library
register = Library()

@register.simple_tag
def trip_image(trip):
    state = trip.start_loc.address_state.upper()
    img = "<img src='/static/images/states/%s.jpg'/>" % state
    return img