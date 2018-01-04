from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^new$', views.EmployeeCreateView.as_view(), name='new-employee'),
    url(r'^list$', views.EmployeeListView.as_view(), name='employees-list'),
    url(r'^update/(?P<pk>\d+)$', views.EmployeeUpdateView.as_view(), name='employee-update'),
    url(r'^reports$', views.reports, name="reports"),
    url(r'^transfers/(?P<pk>\d+)$', views.EmployeeTransfersView.as_view(), name='employee-transfers'),
    url(r'^new_transfer_form/(?P<pk>\d+)$', views.EmployeeCreateNewTransferView.as_view(), name='employee-new-transfer'),
    url(r'^promotions/(?P<pk>\d+)$', views.EmployeePromotionsView.as_view(), name='employee-promotions'),
    url(r'^promote/(?P<pk>\d+)$', views.EmployeePromoteView.as_view(), name='employee-promote'),
    url(r'^documents/(?P<pk>\d+)$', views.EmployeeDocuments.as_view(), name='employee-documents'),
    url(r'^new_document_form/(?P<pk>\d+)$', views.EmployeeAddNewDocument.as_view(), name='employee-add-new-document'),
    url(r'^leaves/(?P<pk>\d+)$', views.EmployeeLeavesView.as_view(), name='employee-leaves'),
    url(r'^new_leave_form/(?P<pk>\d+)$', views.EmployeeCreateLeaveFormView.as_view(), name='employee-new-leave'),
    url(r'^details/(?P<pk>\d+)$', views.EmployeeDetailView.as_view(), name='employee-detail'),
]
