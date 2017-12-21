from django.conf.urls import url
from . import views


urlpatterns = [
             
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^list$', views.list_employees, name='employees'),
    url(r'^edit/(?P<pk>\d+)/$', views.employee_edit, name="employee_edit"),
    
]
