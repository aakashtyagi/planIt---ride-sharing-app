import uuid

from django import forms
from django.db.models import Field, SubfieldBase
from django.db.models.fields import *
from django.db.models import ImageField, FileField, FilePathField

try:
    from django.utils.encoding import smart_unicode
except ImportError:
    from django.utils.encoding import smart_text as smart_unicode


class UUIDField(Field):
    """
    A field which stores a UUID value in hex format. This may also have the
    Boolean attribute 'auto' which will set the value on initial save to a new
    UUID value. Note that while all UUIDs are expected to be unique we enforce
    this with a DB constraint.
    """
    # TODO: support binary storage types
    __metaclass__ = SubfieldBase

    def __init__(self, auto=True, *args, **kwargs):
        #print 'UUID Init'
        self.auto = auto

        if auto:
            kwargs['editable'] = False
            kwargs['blank'] = True
            kwargs['unique'] = True
        super(UUIDField, self).__init__(*args, **kwargs)

    #def deconstruct(self):
        #print 'UUID Deconstruct'
        #name, path, args, kwargs = super(UUIDField, self).deconstruct()
        #del kwargs['max_length']

        #if self.auto:
        #    kwargs.pop('editable')
        #    kwargs.pop('blank')
        #    kwargs.pop('unique')
        #    kwargs['auto'] = True

    def _create_uuid(self):
        #print 'UUID Create'
        return uuid.uuid4().hex

    def db_type(self, connection=None):
        #print 'UUID DB Type'
        return 'char(50)'

    def pre_save(self, model_instance, add):
        #print 'UUID Pre Save'
        """
        This is used to ensure that we auto-set values if required.
        See CharField.pre_save
        """
        value = getattr(model_instance, self.attname, None)
        if self.auto and add and not value:
            value = self._create_uuid()
            setattr(model_instance, self.attname, value)
        return value
    #
    # def get_db_prep_value(self, value, connection, prepared=False):
    #     print 'UUID Get DB Prep Value'
    #     """
    #     Casts uuid.UUID values into the format expected by the back end
    #     """
    #     if isinstance(value, uuid.UUID):
    #         value = str(value)
    #     if isinstance(value, str):
    #         if '-' in value:
    #             value = value.replace('-', '')
    #         uuid.UUID(value) # raises ValueError with invalid UUID format
    #     return value

    # def value_to_string(self, obj):
    #     print 'UUID Value to String'
    #     val = self._get_val_from_obj(obj)
    #     if val is None:
    #         data = ''
    #     else:
    #         data = str(val)
    #     return data

    # def to_python(self, value):
    #     print 'UUID to python'
    #     """
    #     Returns a ``StringUUID`` instance from the value returned by the
    #     database. This doesn't use uuid.UUID directly for backwards
    #     compatibility, as ``StringUUID`` implements ``__unicode__`` with
    #     ``uuid.UUID.hex()``.
    #     """
    #     if not value:
    #         return None
    #     else:
    #         return str(value)
    #     # attempt to parse a UUID including cases in which value is a UUID
    #     # instance already to be able to get our StringUUID in.
    #     #return StringUUID(smart_unicode(value), hyphenate=self.hyphenate)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.CharField,
            'max_length': 50,
        }
        defaults.update(kwargs)
        return super(UUIDField, self).formfield(**defaults)

# try:
#     from south.modelsinspector import add_introspection_rules
#     add_introspection_rules([], [r"^uuidfield\.fields\.UUIDField"])
# except ImportError:
#     pass