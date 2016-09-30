# -*- coding: utf-8 -*-
from django.db.models import *
from django.utils.translation import ugettext_lazy as _


SIMPLE_FIELDS = (
    BigIntegerField,
    BinaryField,
    BooleanField,
    CharField,
    CommaSeparatedIntegerField,
    DateField,
    DateTimeField,
    DecimalField,
    DurationField,
    EmailField,
    FileField,
    FilePathField,
    FloatField,
    ImageField,
    IntegerField,
    GenericIPAddressField,
    NullBooleanField,
    PositiveIntegerField,
    PositiveSmallIntegerField,
    SlugField,
    SmallIntegerField,
    TextField,
    URLField,
    UUIDField,
)

RELATION_FIELDS = (
    ForeignKey,
    OneToOneField,
)

ADVANCED_RELATION_FIELDS = (
    ManyToManyField,
)

BLACKLIST_FIELDS = (
    'uuid',
    '_order',
    'is_draft',
    'draft_of',
    'has_draft',
    'created',
    'modified',
)


def clone_fields(instance, draft):
    print("Clone field relations for %s from %s (class: %s)" % (instance, draft, instance.__class__.__name__))

    # get all fields from model
    model_fields = instance._meta.get_fields()
    print(instance)

    # set instance fields
    for field in model_fields:

        # set simple instance attribute
        if type(field) in SIMPLE_FIELDS and field.name not in BLACKLIST_FIELDS:
            print("set: %s (%s)" % (getattr(draft, field.name, None), field.name))
            setattr(instance, field.name, getattr(draft, field.name, None))

        # set relation fields

        # set relation advanced fields

    instance.save()
    return instance


def clone_fk(instance, copy):
    print("Clone foreignkey relations for %s (class: %s)" % instance, instance.__class__.__name__)
    return


def clone_m2m(instance, copy):
    print("Clone m2m relations for %s (class: %s)" % instance, instance.__class__.__name__)
    return