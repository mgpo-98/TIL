from dataclasses import field
import imp
from django.contrib.auth.forms import UserCreationForm
from dataclasses import fields
from .models import User
from django.contrib.auth import get_user_model


class CusetomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username',)