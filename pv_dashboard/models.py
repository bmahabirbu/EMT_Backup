from django.db import models
import pandas as pd

from django.utils.translation import gettext as _
 
from django_pandas.managers import DataFrameManager

#name of table
class TimeSeries(models.Model):
    # add all field names
    Date = models.CharField(_('Date'), max_length=100)
    Time = models.TimeField(_('Time'))
    Temp = models.FloatField(_('Temperature'))
    Humidity = models.FloatField(_('Humidity'))
    GPOA = models.FloatField(_('GPOA(W/M2)'))
    panel = models.CharField(_('EDS/CTRL(#)'), max_length=100)

    Voc_Before = models.FloatField(_('Voc_Before(V)'))
    Voc_After = models.FloatField(_('Voc_After(V)'))

    Isc_Before = models.FloatField(_('Isc_Before(A)'))
    Isc_After = models.FloatField(_('Isc_After(A)'))

    Pout_Before = models.FloatField(_('Pout_Before(W)'))
    Pout_After = models.FloatField(_('Pout_After(W)'))

    PR_Before = models.FloatField(_('PR_Before'))
    PR_After = models.FloatField(_('PR_After'))

    SI_Before = models.FloatField(_('SI_Before'))
    SI_After = models.FloatField(_('SI_After'))

    #turns the model into a datafame to return to views and edit
    objects = DataFrameManager()