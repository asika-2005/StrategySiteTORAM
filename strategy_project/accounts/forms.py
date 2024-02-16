from typing import Any
from .models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            "email",
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


# class LoginForm(AuthenticationForm):

#     class Meta:
#          model = User
#          fields = ('username', 'password',)
#     def __init__(self, *args, **kwargs):
#         super().__init__(args,kwargs)
#         for field in self.fields.values():
#             field.widget.attrs["class"] = "form-control"
#         self.fields['username'].widget.attrs['placeholder'] = 'username'
#         self.fields['password'].widget.attrs['placeholder'] = 'password'

class LoginForm(AuthenticationForm):
    class Meta:
        model = User