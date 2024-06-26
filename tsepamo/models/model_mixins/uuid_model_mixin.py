import uuid

from django.db.models.fields import UUIDField
from django.db import models


class UUIDAutoField(UUIDField):
    """ AutoField for Universally unique identifier.
    """
    def pre_save(self, model_instance, add):
        value = super(UUIDAutoField, self).pre_save(model_instance, add)
        if add and value is None:
            value = uuid.uuid4()
            setattr(model_instance, self.attname, value)
        else:
            if not value:
                value = uuid.uuid4()
                setattr(model_instance, self.attname, value)
        return value


class UuidModelMixin(models.Model):
    """ Base model class for all models using an UUID and not
        an INT for the primary key.
    """

    id = UUIDAutoField(
        blank=True,
        editable=False,
        help_text="System auto field. UUID primary key.",
        primary_key=True)

    class Meta:
        abstract = True
