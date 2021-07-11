from address_book.models import Contact
from django.contrib.auth.models import User
from .serializers import ContactSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly


class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
