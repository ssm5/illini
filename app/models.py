from __future__ import unicode_literals

from django.db import models

from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Tag(models.Model):
    TAG_BREADTHS = (
        ('B', 'BROAD'),
        ('S', 'SPECIFIC'),
        ('N', 'NICHE')
    )
    name = models.CharField(_('Tag'), max_length=64, unique=True)
    breadth = models.CharField(_('Breadth'), max_length=1, choices=TAG_BREADTHS, default='N')
    # organizationCount = models.IntegerField(_('Organization Count'), default=0)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        ordering = ['name']


class Organization(models.Model):
    tags = models.ManyToManyField(Tag)
    name = models.CharField(_('Name'), max_length=64, unique=True)
    abbr = models.CharField(_('Abbreviation'), max_length=10, unique=True, null=True, blank=True, default='')
    found_date = models.DateTimeField(_('Date Founded'))
    end_date = models.DateTimeField(_('Date Ended'), null=True, blank=True)
    summary = models.TextField(_('Summary'), max_length=256, default='')
    description = models.TextField(_('Description'), default='')
    logo = models.ImageField(_('Logo'), blank=True, null=True)
    members = models.IntegerField(_('Number of Members'), default=0)
    email = models.EmailField(_('Organization Email'), null=True, blank=True)
    is_public = models.BooleanField(_('Is Public'), default=False)
    last_modified = models.DateTimeField(_('Last Modified'), null=True, blank=True, auto_now_add=True)
    is_deleted = models.BooleanField(_('Deleted'), default=False)

    def __str__(self):
        return self.name + (" (" + self.abbr + " )" if self.abbr else "")

    def __unicode__(self):
        return self.name + (" (" + self.abbr + " )" if self.abbr else "")

    class Meta:
        verbose_name = _('RSO')
        verbose_name_plural = _('RSOs')
        ordering = ['name']
        unique_together = ['name', 'abbr']

