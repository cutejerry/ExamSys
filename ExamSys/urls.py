"""ExamSys URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from . import view
from SubjectsModel import views as SubjectsModel_views

urlpatterns = [
    url(r'^$', view.hello),
    url(r'^exam/', SubjectsModel_views.choose_exam),
    url(r'^exampaper/', SubjectsModel_views.make_exam),
    url(r'^exam_marking/', SubjectsModel_views.mark_exam),
    url(r'^recommend/', SubjectsModel_views.show_recommend),
    url(r'^admin/', admin.site.urls),
]
