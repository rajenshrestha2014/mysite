from django.conf.urls import url,include

from BikeDetails.views import add_new_bike,BikeDetailView
from . import views

urlpatterns = [
    url(r'^$', views.BikeHomeView, name ='BikeHomeView'),
     url(r'^new/$', views.add_new_bike, name='add_new_bike'),
    url(r'^bike/(?P<pk>\d+)/$', BikeDetailView.as_view(), name='bike_detail'),

]