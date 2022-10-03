# django imports
from django.urls import path

# project imports
from stats import views

urlpatterns = [
    path('', views.developer_list, name='developer_list'),

    # developer urls
    path('create/', views.developer_create, name='developer_create'),
    path('<str:username>/', views.developer_detail, name='developer_detail'),

    # repos urls

]
