from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.CurriculumViewSet.as_view({'get': 'list', 'post': 'create', })),
    url(r'^(?P<pk>\d+)/$', views.CurriculumViewSet.as_view({'get': 'retrieve', })),
    url(r'^list$', views.FixedCoachTimeCurriculum.as_view({'get': 'list', })),
]
