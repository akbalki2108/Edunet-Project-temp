from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Zomato(models.Model):
    name = models.CharField(_("name"),max_length=255)
    online_order = models.CharField(_("online_order"),max_length=255)
    book_table = models.CharField(_("book_table"),max_length=255)
    rate = models.FloatField(_("rate"))
    votes = models.IntegerField(_("votes"))
    location = models.CharField(_("location"),max_length=255)
    rest_type = models.CharField(_("rest_type"),max_length=255)
    cuisines = models.CharField(_("cuisines"),max_length=255)
    cost2plates = models.IntegerField(_("cost2plates"))
    listed_in_type = models.CharField(_("listed_in_type"),max_length=255)
    area = models.CharField(_("area"),max_length=255)


