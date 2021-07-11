from django.urls import path
from . import views

urlpatterns = [
    path('contacts', views.ContactList.as_view(), name='contact-list'),
    path('contacts/<int:pk>', views.ContactDetail.as_view(), name='contact-detail')
]
