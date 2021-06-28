from django.urls import path
from .views import (
    home,
    ContactListView,
    ContactCreateView,
    ContactDetailView
)
'''
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
'''

urlpatterns = [
    path('', home, name='address_book-home'),
    path('user/<str:username>', ContactListView.as_view(), name='user-contacts'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/new', ContactCreateView.as_view(), name='contact-create')
]