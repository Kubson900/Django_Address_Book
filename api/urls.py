from django.urls import path
from . import views

urlpatterns = [
    path('contacts', views.ContactList.as_view(), name='contact-list'),
    path('contacts/<int:pk>', views.ContactDetail.as_view(), name='contact-detail'),
    path('users', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail')
]
