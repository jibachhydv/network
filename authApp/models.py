from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.db import models

from .manager import CustomUserModelManager, CustomUserManager

from django.core.exceptions import ValidationError


class CustomUserModel(AbstractBaseUser, PermissionsMixin):

    # first name
    first_name = models.CharField(max_length=255, verbose_name="First Name")

    # last name
    last_name = models.CharField(max_length=255, verbose_name="Last Name")

    # email
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    # Is Active or Not
    is_active = models.BooleanField(default=True)

    # Is Admin of the site
    is_admin = models.BooleanField(default=False)

    # Is Staff of the site
    # is_staff = models.BooleanField(default=False)

    # user name field
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    # Custom Manager
    # objects = CustomUserModelManager()
    objects = CustomUserManager()

    @property
    def is_staff(self):
        return self.is_admin

    # str repr
    def __str__(self):
        return self.email

    # get Short Name
    def get_short_name(self):
        return self.first_name

    # get full name
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, alwaysz
        return self.is_admin

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin


# Following model
class FollowingModel(models.Model):

    # Who Is Following
    follower = models.ForeignKey(
        CustomUserModel, on_delete=models.CASCADE, related_name="follower")

    # To Whom he is following
    following = models.ForeignKey(
        CustomUserModel, on_delete=models.CASCADE, related_name="following")

    def __str__(self):
        return f"{self.follower} follows {self.following}"

    def clean(self):
        if self.follower == self.following:
            raise ValidationError("Cannot follow themselves")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['follower', 'following'], name="unique_followers")
        ]
