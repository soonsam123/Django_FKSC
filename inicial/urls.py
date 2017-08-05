from django.conf.urls import url
from . import views

app_name = 'inicial'

urlpatterns = [
    #/
    url(r'^$', views.index, name='index'),

    #/contato/
    url(r'^contato/$', views.contato, name='contato'),

    #/ranking/
    url(r'^ranking/$', views.ranking, name='ranking'),
]