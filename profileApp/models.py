from uuid import uuid4
from django.utils.deconstruct import deconstructible
from django.db import models
from django.contrib.auth import get_user_model

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
import os

User = get_user_model()


@deconstructible
class UploadTo(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.sub_path, filename)


class Profile(models.Model):

    # User
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile',)

    # Profile Picture
    profile_picture = models.ImageField(
        verbose_name="Profile picture", upload_to='profile_photo', blank=True, null=True)

    # DOB
    dob = models.DateField(verbose_name="Date of Birth", blank=True, null=True)

    # school name
    school_name = models.CharField(
        verbose_name="School Name", max_length=500, blank=True, null=True)

    def __str__(self):
        return f"Profile of {self.user}"

    
    def save(self, *args, **kwargs):

        if self.profile_picture:
            self.profile_picture = self.compressImage(self.profile_picture)

        super(Profile, self).save(*args, **kwargs)

    def compressImage(self, uploadedImage):
        imageTemproary = Image.open(uploadedImage)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize((300, 300))
        imageTemproaryResized.save(outputIoStream, format='JPEG', quality=100)
        outputIoStream.seek(0)
        uploadedImage = InMemoryUploadedFile(outputIoStream, 'ImageField', "%s.jpg" % uploadedImage.name.split('.')[
                                             0], 'image/jpeg', sys.getsizeof(outputIoStream), None)
        return uploadedImage
