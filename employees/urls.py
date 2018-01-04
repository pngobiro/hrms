from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^new$', views.EmployeesCreateView.as_view(), name='new_employee'),
    url(r'^list$', views.EmployeesListView.as_view(), name='employees-list'),
    url(r'^reports$', views.reports, name="reports"),
    url(r'^transfers/(?P<pk>\d+)$', views.EmployeesTransfersView.as_view(), name='employee-transfers'),
    url(r'^promotions$', views.EmployeesPromotionsView.as_view(), name='employee-promotions'),
    url(r'^leaves$', views.EmployeesLeavesView.as_view(), name='employee-leaves'),
    url(r'^details/(?P<pk>\d+)$', views.EmployeesDetailView.as_view(), name='employee-detail'),
]
