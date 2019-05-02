from django.conf.urls import url
from automata import views


urlpatterns = [
    url(r'evaluar/(?P<palabra>[abc]+)', views.evaluador),
]