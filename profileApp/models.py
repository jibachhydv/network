from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):

    # User
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile',)

    # Profile Picture
    profile_picture = models.ImageField(verbose_name="Profile picture")

    # DOB
    dob = models.DateField(verbose_name="Date of Birth")

    # school name
    school_name = models.CharField(verbose_name="School Name", max_length=500)

    def __str__(self):
        return f"Profile of {self.user}"
