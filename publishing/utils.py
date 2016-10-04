# -*- coding: utf-8 -*-
from django.db.models import *


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
    ManyToOneRel,
)

ADVANCED_RELATION_FIELDS = (
    OneToOneField,
)

BLACKLIST_FIELDS = (
    'draft',
    'is_draft',
    'draft_of',
    'has_draft',

    'uuid',
    '_order',
    'created',
    'modified',
)


def clone_fields(instance, draft):
    # print("Clone field relations for '%s' from '%s' (class: %s)" % (instance, draft, instance.__class__.__name__))

    # get all fields from model
    model_fields = instance._meta.get_fields()

    # set instance fields
    for field in model_fields:

        # set simple instance attribute
        if type(field) in SIMPLE_FIELDS and field.name not in BLACKLIST_FIELDS:
            setattr(instance, field.name, getattr(draft, field.name, None))

        # set relation fields
        instance.save()
        if type(field) in RELATION_FIELDS and field.name not in BLACKLIST_FIELDS:
            instance, draft = clone_relations(instance, draft, field)

    instance.save()
    return instance


def clone_relations(instance, copy, field):
    related_instance_items = getattr(copy, field.name).all()

    for item in related_instance_items:
        new_item = item.__class__()
        new_item = clone_fields(new_item, item)
        getattr(instance, field.name).add(new_item)
        new_item.is_draft = True
        new_item.draft_of = item
        new_item.save()

    return instance, copy
