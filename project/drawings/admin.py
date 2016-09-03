from django.contrib import admin

from .models import Notebook, Drawing, GroupDrawing, Group, ArtistInfo


class GroupDrawingInline(admin.TabularInline):
    """Inline of groups on drawing admin."""

    model = GroupDrawing

    fields = ['group']

    extra = 1


@admin.register(Group)
class Group(admin.ModelAdmin):
    """Group admin form."""

    fieldsets = [
        ('', {
            'fields':[
                'id',
                'name',
                'description',
            ]
        }),
    ]

    list_display = ['name']
    list_display_links = ['name']




@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    """Notebook admin form."""

    fieldsets = [
        ('', {
            'fields': [
                'id',
                'title',
                'description',
                'front_cover',
                'back_cover',
                'drawn_at',
             ]

        }),
        ('Advanced', {
            'fields': [
                'created',
                'modified',
            ],
            'classes': ['collapse']
        })
    ]

    search_fields = ["title", "description", "id"]

    list_display = ['title']
    list_display_links = ['title']


    def get_readonly_fields(self, request, obj=None):
        """Make changing the id impossible once published."""

        readonly = ['created', 'modified']

        if obj:
            readonly.append('id')

        return readonly


@admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin):
    """Drawing admin form."""

    fieldsets = [
        ('', {
            'fields': [
                'notebook',
                'title',
                'id',
                'favorite',
                'image',
                'description',
            ]
        }),
        ('Advanced', {
            'fields': [
                'created',
                'modified',
            ],
            'classes': ['collapse']
        })
    ]

    list_display = ['title', 'notebook']
    list_display_links = ['title', 'notebook']
    inlines = [GroupDrawingInline]

    def get_readonly_fields(self, request, obj=None):
        """Make changing the id impossible once published."""

        readonly = ['created', 'modified']

        if obj:
            readonly.append('id')

        return readonly


@admin.register(ArtistInfo)
class ArtistInfoAdmin(admin.ModelAdmin):
    """Artist info admin form."""

    fieldsets = [
        ('', {
            'fields': [
                'description',
                'contact',
            ]
        }),
        ('Advanced', {
            'fields':[
                'created',
                'modified',
            ],
            'classes':['hidden']
        })
    ]

    list_display = ['created']

    def get_readonly_fields(self, request, obj=None):
        """Make changing the id impossible once published."""

        readonly = ['created', 'modified']

        if obj:
            readonly.append('id')

        return readonly






