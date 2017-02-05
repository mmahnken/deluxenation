
"""Views for drawings product."""

from django.conf.urls import url

from . import views

# So we don't have to write this out each time; this is a legal Django slug regex.
PK = "(?P<pk>[a-zA-Z0-9][a-zA-Z0-9-_]*)"


urlpatterns = [

    #####################################################
    # Cohorts
    #
    # /             dashboard of current cohort
    # /cohort/f12   dashboard of named cohort


url(r'^$',
    views.HomepageView.as_view(),
    name='homepage'),

url(r'^years/$',
    views.NotebooksByYearView.as_view(),
    name='notebooks_by_year'),

url(r'^notebooks/$',
    views.NotebookListView.as_view(),
    name='notebooks'),

url(r'^notebooks/%s/$' % PK,
    views.NotebookView.as_view(),
    name='notebook_detail'),

url(r'^groups/all/$',
    views.GroupListView.as_view(),
    name='groups'),

url(r'^nb/all/$',
    views.NotebookListJSONView.as_view(),
    name='notebooks'),

]



