from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from audit_log.models import AuthStampedModel
from django_extensions.db.models import TimeStampedModel
from mb_database.fields import UUIDField, EmailField, CharField
from django.db.models import Model, ForeignKey, ManyToManyField, CASCADE, Manager
from django.utils.text import slugify

class DataModel(Model):
    id = UUIDField(primary_key=True, auto=True)

    class Meta:
        abstract = True

class SecureDataModel(DataModel, AuthStampedModel, TimeStampedModel):

    class Meta:
        abstract = True

class SlugModel(Model):
    name = CharField(max_length=100, default=None, null=True)
    slug = CharField(max_length=100, default=None, blank=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify( self.name )
        super(SlugModel, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.name


class EmployeeManager(UserManager):

    def all(self):
        return self.filter(is_active=True)

    def create_user(self, email=None, password=None):
        #if not username:
        #    raise ValueError('Users must have a username')

        email = UserManager.normalize_email(email)
        user = self.model(email=email, password=password)
        #user = User(username=username, email=email)
        #user.username = username
        user.is_superuser = False
        user.set_password(password)
        #user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        u = self.create_user(email=email, password=password)
        u.is_admin = True
        u.is_staff = True
        u.is_superuser = True
        u.is_active = True
        u.save(using=self._db)
        return u

class EmailUserModel(DataModel, AbstractBaseUser):
    email = EmailField(default=None, unique=True, blank=False, null=True, max_length=100)

    class Meta:
        abstract = True
