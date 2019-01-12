"""pc URL Configuration

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
# from django.contrib import admin
from rest_framework import routers
from book import views as bookview
from account import views as accountview
from xadmin.plugins import xversion
import xadmin
xadmin.autodiscover()
xversion.register_models()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'books', bookview.BookInformationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^xadmin/', xadmin.site.urls),
    # url(r'^admin/', admin.site.urls),
    url(r'^books/', include('book.urls')),
    url(r'^auth/$', accountview.UsersView.as_view()),
    url(r'^product/', include('curriculum.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]