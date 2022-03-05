from rest_framework import serializers
from address_book.models import Contact
from django.contrib.auth.models import User


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    contacts = serializers.PrimaryKeyRelatedField(many=True, queryset=Contact.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'contacts']
