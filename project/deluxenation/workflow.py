"""Workflow tools."""

from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.messages.api import add_message
from django.core.exceptions import ValidationError
from django.db import transaction

_private = ('private', 'Private')
_published = ('published', 'Published')

#: Our standard workflow order
WORKFLOW_STATUS = [_private, _published]

#: Our workflow order for things which should begin as published
WORKFLOW_STATUS_PUBLISH_DEFAULT = [_published, _private]


def make_published(modeladmin, request, queryset):
    """Action for administrative interface to publish.

    Note that this is intentionally implemented in a less efficient way; this could be
    done with a QuerySet method of::

      queryset.update(status='published')

    However, this does not emit post_save events, which are needed by our search indexing
    system---so we do it in a less-efficient way that does trigger this required update.
    """

    with transaction.atomic():
        for o in queryset.all():
            o.status = 'published'
            try:
                o.full_clean()
                o.save()
            except ValidationError as e:
                # We can't publish this, so we'll let the user know via messages
                add_message(
                        request,
                        messages.ERROR,
                        "Could not publish %s (%s): %s" % (
                            str(o), o.pk, ", ".join(e.messages)))


make_published.short_description = 'Publish'


def make_private(modeladmin, request, queryset):
    """Action for administrative interface to hide things.

    See note in :py:func:`make_published` about efficiency.
    """

    with transaction.atomic():
        for o in queryset.all():
            o.status = 'private'
            o.save()


make_private.short_description = 'Make private'


#: Importable list of actions to use in app's model admin classes
admin_workflow_actions = [make_private, make_published]
