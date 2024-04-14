# NetworkVisualisationToolWebsite/urls.py
from django.urls import path
from NetworkVisualisationToolWebsite import views 

urlpatterns = [
    path("", views.home, name='home', kwargs={'empty_search' : ''}),
    path("<int:empty_search>", views.home, name='home'),
    path("about/", views.about, name="about"),
    path("how-to/", views.howto, name="how-to"),
    path("test/", views.test, name="test"),
    path("applyFiltrationOptions/<str:filterCategory1>/<str:filterParameter1>/<str:filterCategory2>/<str:filterParameter2>", views.applyFiltrationOptions, name="applyFiltrationOptions"),
    path("resetFiltrationOptions/", views.resetFiltrationOptions, name="resetFiltrationOptions")
]
