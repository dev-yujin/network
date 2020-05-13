from django.conf.urls import url
from feedback import views
 
urlpatterns = [
    url(r'^list', views.list, name='list'),
    url(r'^$', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
]
# </id>