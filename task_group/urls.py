from django.conf.urls import url
from task_group import views
from django.urls import path
from task_group.views import  TaskListView, CatagoriesDetailView, \
    CatagoriesCreateView,  TaskCreateView, CatagoriesDeleteView,TaskDeleteView,TaskUpdateView

app_name='task_group'
urlpatterns = [
    path('',TaskListView.as_view(),name='tlist'),
    path('tasklist/',TaskListView.as_view(),name='tlist'),
    path('task_update/<int:pk>/',TaskUpdateView.as_view(),name='t_create'),
    path('details/<str:pk>/', CatagoriesDetailView.as_view(), name='cdetail'),
    path('catagories_delete/<str:pk>/', CatagoriesDeleteView.as_view(), name='c_delete'),
    path('catagories_create/',CatagoriesCreateView.as_view(),name='c_create'),
    path('task_create/',TaskCreateView.as_view(),name='t_create'),
    path('task_delete/<int:pk>/', TaskDeleteView.as_view(), name='t_delete')

]