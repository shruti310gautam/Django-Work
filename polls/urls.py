from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^ajax/more/$', views.todo, name='contact'),
    url(r'^ajax/display/$', views.more, name='contact'),
    #url(r'^signup/$', views.SignUpView.as_view(), name='signup'),
    #url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
]
