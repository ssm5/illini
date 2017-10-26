from __future__ import unicode_literals

from django.db import models

from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Organization(models.Model):
    name = models.CharField(_('Name'), max_length=200)
    found_date = models.DateField(_('Date Founded'))
    description = models.TextField(_('Description'), default='')
    logo = models.ImageField(_('Logo'), blank=True, null=True)
    members = models.IntegerField(_('Number of Members'), default=0)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('RSO')
        verbose_name_plural = _('RSOs')

