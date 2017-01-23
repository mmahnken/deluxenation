"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.conf.urls.static import static

import drawings.urls
import drawings.views

import settings


urlpatterns = [
    url(r'^admin/nb/$', staff_member_required(drawings.views.NotebookCreateView.as_view(template_name='drawings/notebook_create.html'))),
    url(r'^admin/bulk-add/drawings/$', staff_member_required(drawings.views.BulkDrawingCreateView.as_view(template_name='drawings/bulk-add.html'))),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(drawings.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



