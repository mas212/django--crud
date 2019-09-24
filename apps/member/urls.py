from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('store', views.store, name='store'),
    path('edit/<int:member_id>', views.edit, name='edit'),
    path('update/<int:member_id>', views.update, name='update'),
    path('delete/<int:member_id>', views.delete, name='delete'),
]