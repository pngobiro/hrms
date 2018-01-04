from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^new$', views.EmployeesCreateView.as_view(), name='new_employee'),
    url(r'^list$', views.EmployeesListView.as_view(), name='employees-list'),
    url(r'^update/(?P<pk>\d+)$', views.EmployeesUpdateView.as_view(), name='employee-update'),
    url(r'^reports$', views.reports, name="reports"),
    url(r'^transfers/(?P<pk>\d+)$', views.EmployeesTransfersView.as_view(), name='employee-transfers'),
    url(r'^promotions/(?P<pk>\d+)$', views.EmployeesPromotionsView.as_view(), name='employee-promotions'),
    url(r'^documents/(?P<pk>\d+)$', views.EmployeesPromotionsView.as_view(), name='employee-documents'),
    url(r'^leaves/(?P<pk>\d+)$', views.EmployeesLeavesView.as_view(), name='employee-leaves'),
    url(r'^details/(?P<pk>\d+)$', views.EmployeesDetailView.as_view(), name='employee-detail'),
]
