from django.db import models

from django.utils.translation import gettext as _
# Create your models here.

class Sightings(modelmodel):
    Latitude = models.FloatField(
            max_length = 100,
            help_text=_('Latitude'),
            )
    Longitude = models.FloatField(
        max_length = 100,
        help_text=_('Longitude'),
        )
    Unique_Squirrel_ID = CharField(
            max_length = 50,
            help_text=_('Squirrel_ID'),
            )

    PM = 'pm'
    AM = 'am'
    OTHER = 'other'
    SHIFT_CHOICES=(
            (PM,'PM'),
            (AM,'AM'),
            (OTHER,'Other'),
            )
    Shift = model.CharField(
            max_length=3,
            choices= SHIFT_CHOICES,
            default = OTHER,
            )

    Date = models.DateField(
            help_text=_('Bday of pet'),
            )

    Running = model.BooleanField(
            default = False,
            help_text = _('Whether running?'),
            )

