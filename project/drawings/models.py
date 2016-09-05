from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from model_utils.models import TimeStampedModel

import random


class Notebook(TimeStampedModel, models.Model):

    id = models.SlugField(
        primary_key=True,
        max_length=20,
        help_text="Abbreviated code for a notebook",
    )

    title = models.CharField(
        blank=True,
        help_text="Optional title for noteboook.",
        max_length=300,
    )

    description = models.TextField(
        blank=True,
        help_text="More information about this notebook.",
    )

    front_cover = models.ImageField(
        upload_to="notebooks",
        help_text="Image of notebook's front cover",
    )

    back_cover = models.ImageField(
        upload_to="notebooks",
        help_text="Image of notebook's back cover",
    )

    drawn_at = models.DateField(
        blank=True,
        help_text="The date (month, year) when the notebook was created. Both month and year required.",
        verbose_name="Notebook creation month and year"
    )

    def __str__(self):
        return self.title

    @property
    def random_favorite(self):
        favorites = [d for d in self.drawing_set.all() if d.favorite]
        return random.choice(favorites)



class Drawing(TimeStampedModel, models.Model):
    """A single page of a notebook."""

    # group foreign key

    notebook = models.ForeignKey(
        Notebook,
    )

    title = models.CharField(
        max_length=200,
        blank=True,
        help_text="The title of the drawing."
    )


    id = models.SlugField(
        primary_key=True,
        max_length=20,
        help_text="Abbreviated code for a drawing.",
    )

    favorite = models.BooleanField(
        default=False,
        help_text="If true, this is a favorite drawing in a notebook.",
    )

    image = models.ImageField(
        blank=False,
        upload_to="drawings",
        help_text="High-quality JPEG of drawing",
    )

    description = models.TextField(
        blank=True,
        help_text="Description of the drawing"
    )

    def get_absolute_url(self):
        """URL of drawing detail page."""

        return reverse('drawing_detail', kwargs={'pk': self.id})


class Group(models.Model):
    """A group of drawings"""

    id = models.SlugField(
        max_length=25,
        primary_key=True,
        help_text="Abbreviated unique code for this group.",
    )

    name = models.CharField(
        max_length=35,
        blank=True,
    )

    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        return self.name


class GroupDrawing(models.Model):
    """Association between drawing and groups."""

    group = models.ForeignKey(Group)

    drawing = models.ForeignKey(Drawing)


class ArtistInfo(TimeStampedModel, models.Model):
    """Artistic bio and mission statement for About The Artist page."""

    description = models.TextField(
        blank=False,
        help_text="Text to show for About The Artist page."
    )

    contact = models.CharField(
        blank=True,
        help_text="Optional information to contact the artist.",
        max_length=200,
    )
