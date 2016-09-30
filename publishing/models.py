# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class PublishingProfile(models.Model):
    """
    A user profile
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', )
    regions = models.ManyToManyField("PublishingRegion", through="PublishingProfileRegion", verbose_name=_(u"Regions"), )

    class Meta:
        app_label = 'publishing'
        verbose_name = _(u"Profile")
        verbose_name_plural = _(u"Profiles")
        ordering = ("user", )


class PublishingProfileRegion(models.Model):
    profile = models.ForeignKey("PublishingProfile", )
    region = models.ForeignKey("PublishingRegion", )
    role = models.CharField(_(u"Role"), max_length=45, default="user", )


class PublishingRegion(models.Model):
    title = models.CharField(_(u"Title"), max_length=255, null=True, )
    countries = models.ManyToManyField("PublishingCountry", verbose_name=_(u"Countries"), )
    languages = models.ManyToManyField("PublishingLanguage", verbose_name=_(u"Languages"), )

    class Meta:
        app_label = 'publishing'
        verbose_name = _(u"Region")
        verbose_name_plural = _(u"Regions")
        ordering = ("title", )


class PublishingCountry(models.Model):
    iso_code = models.CharField(_(u"ISO 639-1 Code"), max_length=2, default="en", )
    title = models.CharField(_(u"Title"), max_length=255, null=True, )

    class Meta:
        app_label = 'publishing'
        verbose_name = _(u"Country")
        verbose_name_plural = _(u"Countries")
        ordering = ("title", )


class PublishingLanguage(models.Model):
    iso_code = models.CharField(_(u"ISO 639-1 Code"), max_length=2, default="en", )
    title = models.CharField(_(u"Title"), max_length=255, null=True, )
    models.ManyToManyField("PublishingLanguage", related_name='languages', )

    class Meta:
        app_label = 'publishing'
        verbose_name = _(u"Language")
        verbose_name_plural = _(u"Languages")
        ordering = ("title", )
