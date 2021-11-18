import uuid
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Vacations, LogList


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4())
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'full_name', 'id_num', 'status', 'password', ]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user


class ProfileCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'full_name', 'first_name', 'last_name', 'third_name', 'phone', 'email', 'id_num',
                  'status']


class VacationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacations
        fields = ['id', 'id_user', 'id_num', 'first_name', 'last_name', 'full_name', 'doc_name', 'start_vacation',
                  'end_vacation', 'vacation_status', 'doc_date']


class LogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogList
        fields = ['id', 'id_user', 'id_num', 'first_name', 'last_name', 'full_name', 'doc_name', 'doc_status',
                  'doc_date']
