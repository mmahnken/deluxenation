
"""Views for drawings product."""

from django.conf.urls import url

from . import views

# So we don't have to write this out each time; this is a legal Django slug regex.
# PK = "(?P<pk>[a-zA-Z0-9][a-zA-Z0-9-_]*)"


urlpatterns = [


url(r'^$',
    views.HomepageView.as_view(),
    name='homepage'),



#########################
# Notebook management

#########################

# url(r'^manage/notebooks/all/$',
#     views.NotebookManagementListView.as_view(),
#     name='notebook_management_list'),
#
# url(r'^manage/notebooks/%s/$' % PK,
#     views.NotebookManagementDetailView.as_view(),
#     name='notebook_management_detail'),


]
