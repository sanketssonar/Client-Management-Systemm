# serializers.py
from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    client = serializers.CharField(source='client.client_name', read_only=True)
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

from django import forms

class UserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, user):
        return user.username

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'client', 'users']

    users = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.SelectMultiple)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['users'].label = 'Select Users'

class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['project_name', 'client', 'users']

    def create(self, validated_data):
        user_ids = validated_data.pop('users')
        project = Project.objects.create(**validated_data)
        project.users.add(*user_ids)
        return project



class ClientSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'created_by', 'updated_at']
