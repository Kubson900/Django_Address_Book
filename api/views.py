from address_book.models import Contact
from .serializers import ContactSerializer
from rest_framework import generics


class ContactList(generics.ListAPIView, generics.GenericAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
