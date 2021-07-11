from django.contrib.auth.base_user import BaseUserManager
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
        user.save(using=self._db)
        return user


class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None):
        ''' 
            Create user with email, first_name and last_name
        '''

        if not email:
            return ValueError("The Email must be set.")

        if not first_name:
            return ValueError("First Name must be provided")

        if not last_name:
            return ValueError("Last Name must be provided")

        email = self.normalize_email(email)

        user = self.model(email=email, first_name=first_name,
                          last_name=last_name)

        user.set_password(password)
        user.save(using=self._db)
        user.is_active = False
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        '''
            Create superuser with email, first_name and last_name
        '''

        user = self.create_user(
            email, first_name, last_name, password=password)
        # user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user
