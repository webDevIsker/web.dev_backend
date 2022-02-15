import uuid
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Vacations, LogList, MawsEditStatus, FormsMaws


class CheckUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'id_num', 'is_active', 'one_off']

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data['password'])
            user.save()
        except KeyError:
            pass
        return user


class CustomUserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4())
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'third_name', 'email', 'email_corp', 'phone',
                  'full_name',
                  'id_num', 'status', 'is_staff', 'is_active', 'one_off']

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.is_active = False
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
        fields = ['id', 'username', 'full_name', 'first_name', 'last_name', 'third_name', 'full_name', 'phone', 'email',
                  'email_corp', 'id_num', 'status']


class VacationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacations
        fields = ['id', 'id_user', 'id_num', 'first_name', 'last_name', 'doc_name', 'start_vacation',
                  'end_vacation', 'vacation_status', 'doc_date', 'vacation_type', 'line_manager', ]


class LogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogList
        fields = ['id', 'id_user', 'id_num', 'first_name', 'last_name', 'doc_name', 'doc_status',
                  'doc_date', 'description', 'tag', ]


class MawsEditStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MawsEditStatus
        fields = ['id', 'id_user', 'user', 'storage', 'placement']


class FormsMawsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormsMaws
        fields = ['id', 'id_user', 'name', 'goods', 'responsibles', 'location', 'storage', 'placement', 'manager',
                  'date']
