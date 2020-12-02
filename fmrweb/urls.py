"""URL configuration
"""
from django.urls import path

from . import views


app_name = 'fmrweb'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'index.html', views.index, name='index-legacy'),
    path(r'faq', views.faq, name='faq'),
    path(r'faq.html', views.faq, name='faq-legacy'),

    path(r'integrator_chains', views.about_integrator_chains, name='about-integrator_chains'),
    path(r'integrator_chains.html', views.about_integrator_chains, name='about-integrator_chains-legacy'),

    path(r'events/challenge-icra2016', views.event_icra2016, name='events-icra2016'),
    path(r'events/challenge-icra2016.html', views.event_icra2016, name='events-icra2016-legacy'),
    path(r'events/workshop-icra2015', views.event_icra2015, name='events-icra2015'),
    path(r'events/workshop-icra2015.html', views.event_icra2015, name='events-icra2015-legacy'),
]
