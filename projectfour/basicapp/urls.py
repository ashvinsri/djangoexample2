from django.conf.urls import url
from basicapp import views

urlpatterns = [url(r'^$',views.SchoolListView.as_view(),name='list'),
               url(r'^(?P<pk>\d+)/$',views.SchoolDetailView.as_view(),name='detail'),
               url(r'^create/$',views.SchoolCreateView.as_view(),name='create'),
               url(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),
]
