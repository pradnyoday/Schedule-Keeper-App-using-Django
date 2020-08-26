from django.urls import path,include
from . import views
from .views import RecordListView,record_create_view

urlpatterns = [
    path('',RecordListView.as_view(),name='record-home'),
    path('add/',record_create_view,name='record-create')
]