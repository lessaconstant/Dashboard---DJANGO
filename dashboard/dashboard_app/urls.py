from django.urls import path
from dashboard_app import views as v1
from importdata import views as v2

urlpatterns =[
    path('', v2.data_extract, name='dashboards'),
    path('<int:id>/', v1.detail_dashboard, name='detail_dashboard'),
]