"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from mysite.views import IndexView, UserCreateView, UserCreateDoneTV

from bookmark.views import BookmarkLV, BookmarkDV, BookmarkCV, BookmarkUV, BookmarkRV
from blog.views import PostLV, PostDV, PostCV, PostUV

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
    url(r'^bookmark/$', BookmarkLV.as_view(), name='bookmark_index'),
    url(r'^bookamrk/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
    url(r'^bookmark/add/$',BookmarkCV.as_view(), name='bookmark_create'),
    url(r'^bookmark/update/(?P<pk>[0-9]+)/$', BookmarkUV.as_view(), name='bookmark_update'),
    url(r'^blog/$', PostLV.as_view(), name='blog_index'),
    url(r'^blog/update/(?P<pk>\d+)/$', PostUV.as_view(), name='post_update'),
    url(r'^blog/(?P<pk>\d+)/$', PostDV.as_view(), name='blog_detail'),
    url(r'^blog/add/$', PostCV.as_view(), name='blog_create'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view()),
    url(r'^bookmark/delete/(?P<pk>[0-9]+)/$', BookmarkRV.as_view(), name='bookmark_delete'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)













