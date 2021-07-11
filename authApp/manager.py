from .models import CustomUserModel
from django.contrib.auth.models import BaseUserManager


class CustomUserModelManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password=None):

        if not email:
            raise ValueError("Users must have an email address")

        if not first_name:
            raise ValueError("Users must have a first name")

        if not last_name:
            raise ValueError("Users must have a last name")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password=None):

        user = self.create_user(first_name=first_name,
                                last_name=last_name, email=email)

        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user
