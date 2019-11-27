from django.db import models

from django.utils.translation import gettext as _
# Create your models here.

class Sightings(models.Model):
    latitude = models.FloatField(
            max_length = 100,
            help_text=_('Latitude'),
            )
    longitude = models.FloatField(
        max_length = 100,
        help_text=_('Longitude'),
        )
    unique_Squirrel_ID = models.CharField(
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
    shift = models.CharField(
            max_length=3,
            choices= SHIFT_CHOICES,
            default = OTHER,
            )

    date = models.DateField(
            help_text=_('Date you saw it'),
            )

    ADULT ='adult'
    JUVENILE = 'juvenile'
    UNKNOWN = 'unknown'
    AGE_CHOICE=(
            (ADULT,'Adult'),
            (JUVENILE,'Juvenile'),
            (UNKNOWN,'Unknown or Blank'),
            )
    age = models.CharField(
        max_length = 20,
        choices = AGE_CHOICE,
        default = UNKNOWN,
        )

    BLACK='black'
    CINNAMON= 'cinamon'
    GRAY = 'gray'
    PRIMARY_FUR_COLOR_CHOICE=(
            (BLACK,'Black'),
            (CINNAMON,'Cinnamon'),
            (GRAY,'Gray'),
            (OTHER,'Unknown or Other'),
            )
    primary_fur_color=models.CharField(
        max_length = 20,
        choices = PRIMARY_FUR_COLOR_CHOICE,
        default = OTHER,
        )


    ABOVE_GROUND='above ground'
    GROUND_PLANE='ground plane'
    LOCATION_CHOICE=(
        (ABOVE_GROUND,'Above Ground'),
        (GROUND_PLANE,'Ground Plane'),
        (OTHER,'Other'),
        )
    location = models.CharField(
        max_length = 50,
        choices = LOCATION_CHOICE,
        default = OTHER,
        )


    specific_location = models.CharField(
        max_length = 1000,
	help_text=_('Specific Location'),
	)

    running = models.BooleanField(
            default = False,
            help_text = _('Whether running?'),
            )
    chasing= models.BooleanField(
            default = False,
            help_text = _('Whether chasing?'),
            )

    climbing= models.BooleanField(
            default = False,
            help_text = _('Whether climbing?'),
            )

    eating= models.BooleanField(
            default = False,
            help_text = _('Whether eating?'),
            )

    foraging= models.BooleanField(
            default = False,
            help_text = _('Whether foraging?'),
            )

    other_activities = models.CharField(
        max_length = 1000,
        help_text=_('Other Activities'),
        )

    kuks = models.BooleanField(
            default = False,
            help_text = _('Whether Kuks?'),
            )
 
    quaas = models.BooleanField(
            default = False,
            help_text = _('Whether Quaas?'),
            )

    moans = models.BooleanField(
            default = False,
            help_text = _('Whether Moans?'),
            )

    tail_flags = models.BooleanField(
                 default = False,
                 help_text = _('Whether Tail Flags?'),
                 )

    tail_twitches = models.BooleanField(
                    default = False,
                    help_text = _('Whether Tail Twitches?'),
                    )

    approaches = models.BooleanField(
                default = False,
                help_text = _('Whether Approaches?'),
                )

    indifferent = models.BooleanField(
                  default = False,
                  help_text = _('Whether indifferent?'),
                  )  

    runs_from = models.BooleanField(
                default = False,
                help_text = _('Whether run from?'),
                )

