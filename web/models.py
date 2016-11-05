from mb_database import fields as f
from mb_database import models as m
from django_countries.fields import CountryField
from django_localflavor_us.models import USStateField
from django.contrib.auth.models import User
from django.db import models

def trip_image_location(instance, filename):
    from uuid import uuid4
    return 'trips/images/' + str(uuid4())


class PlanItModel(m.SecureDataModel):
    class Meta:
        abstract=True

class Location(PlanItModel):
    name = f.CharField(max_length=100, null=True, default=None, blank=False)
    address_1 = f.CharField(default=None, blank=True, null=True, max_length=100)
    address_2 = f.CharField(default=None, blank=True, null=True, max_length=100)
    address_city = f.CharField(default=None, blank=True, null=True, max_length=100)
    address_state = USStateField(default=None, blank=True, null=True)
    address_postal = m.CharField(default=None, blank=True, null=True, max_length=50)
    address_country = CountryField(default=None, blank=True, null=True)


    def __unicode__(self):
        return str(self.id)

class TripManager(m.Manager):

    def all(self):
        return self.filter(open=True)

class Trip(PlanItModel):
    name = f.CharField(max_length=100, null=True, default=None, blank=False)
    descr = f.TextField(max_length=1000, null=True, default=None, blank=True)
    start_loc = m.ForeignKey(Location, null=True, blank=True, default=None, related_name='starting_locations', on_delete=m.CASCADE)
    arrive_loc = m.ForeignKey(Location, null=True, blank=True, default=None, related_name='arriving_locations', on_delete=m.CASCADE)
    return_loc = m.ForeignKey(Location, null=True, blank=True, default=None, related_name='ending_locations', on_delete=m.CASCADE)
    return_home = f.BooleanField(default=True, blank=True)
    start_dt = f.DateTimeField(null=True, blank=False, default=None)
    arrive_dt = f.DateTimeField(null=True, blank=False, default=None)
    return_dt = f.DateTimeField(null=True, blank=False, default=None)
    current_members = f.IntegerField(default=0, blank=True, null=True)
    requested_members = f.IntegerField(default=0, blank=True, null=True)
    open = f.BooleanField(default=False, blank=True, db_column='is_open')

    objects = TripManager()

    class Meta:
        db_table = "trip"

    def add_gas_car(self, user, gas, car, accepted=False):
        p = TripParty()
        p.gas = gas
        p.car = car
        p.trip = self
        p.user = user
        p.accepted = accepted
        p.save()
        self.party.add(p)
        self.save()
        return p

    def add_to_party(self, user, accepted=False):
        p = TripParty()
        p.trip = self
        p.user = user
        p.accepted = accepted
        p.save()
        self.party.add(p)
        self.save()
        return p

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.get_open_seats() == 0:
            self.open = False;
        super(PlanItModel, self).save(*args, **kwargs)

    def get_current_members(self):
        return (self.party.filter(accepted=True).count() + self.current_members) - 1

    def get_open_seats(self):
        # print "test:"
        # print int(self.requested_members) % 2
        return (int(self.requested_members) - self.party.filter(accepted=True).count()) + 1


class TripParty(PlanItModel):
    user = m.ForeignKey(User, default=None, null=True, blank=True)
    trip = m.ForeignKey(Trip, default=None, null=True, blank=True, related_name='party', on_delete=m.CASCADE)
    accepted = f.BooleanField(blank=True, default=False)
    gas = f.BooleanField(blank=True, default=False)
    car = f.BooleanField(blank=True, default=False)

    class Meta:
        db_table = "trip_member"

    def __unicode__(self):
        try:
            return "%s - %s %s" % (self.trip.name, self.user.first_name, self.user.last_name)
        except:
            return str(self.id)

class ActiveEdu(m.Model):
    name = f.CharField(max_length=100, null=True, default=None, blank=False)
    domain = f.CharField(max_length=50, null=True, default=None, blank=False)
    url = f.URLField(max_length=500, null=True, default=None, blank=False)
    active = f.BooleanField(default=True)

    class Meta:
        db_table = "university"

    def __unicode__(self):
        return self.name

class TripCategory(models.Model):
    title = models.CharField(max_length=50, null=True, blank=False, default="Trip Category")
    # pic = models.ImageField(upload_to="static/images/", default = '/static/images/world_map.jpg')
    image_url = models.CharField(max_length=200, null=True)
    alt_tag = models.CharField(max_length=200, null=True)  
    short_desc = models.CharField(max_length=100, null=True, blank=False, default="Short Decription")
    long_Desc = models.CharField(max_length=500, null=True, blank=False, default="Long Decsription")
    url_name = models.CharField(max_length=30, null=True) 

    def __unicode__(self):
        return self.title

class TripPlaces(models.Model):
    category = models.ForeignKey(TripCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True, blank=False, default="Place")
    desc = models.CharField(max_length=300, null=True, blank=False, default="Description")
    image_url = models.CharField(max_length=200, null=True)
    alt_tag = models.CharField(max_length=200, null=True) 

    def __unicode__(self):
        return self.title
    


#----------Extending the existing USER Model------------------

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(max_length=12, default = 0)
    avatar = models.CharField()





















