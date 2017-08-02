from django.conf.urls import url
from . import views

app_name = 'inicial'

urlpatterns = [
    # /inicial/
    url(r'^$', views.index, name='index'),

    #/inicial/contato
    url(r'^contato/$', views.contato, name='contato'),

    #/inicial/ranking
    url(r'^ranking/$', views.ranking, name='ranking'),
]