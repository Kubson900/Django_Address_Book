from django.urls import path
from .views import (
    home,
    ContactListView,
    ContactCreateView,
    ContactDetailView,
    ContactUpdateView,
    ContactDeleteView
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
    path('user/<str:username>', ContactListView.as_view(ordering='name'), name='user-contacts'),
    path('contact/<int:pk>/', ContactDetailView.as_view(), name='contact-detail'),
    path('contact/new', ContactCreateView.as_view(), name='contact-create'),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
]
