from django.db import models
from django.contrib.auth import get_user_model

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

User = get_user_model()


class Profile(models.Model):

    # User
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile',)

    # Profile Picture
    profile_picture = models.ImageField(
        verbose_name="Profile picture", upload_to='profile_photo')

    # DOB
    dob = models.DateField(verbose_name="Date of Birth")

    # school name
    school_name = models.CharField(verbose_name="School Name", max_length=500)

    def __str__(self):
        return f"Profile of {self.user}"

    # def save(self, *args, **kwargs):

    #     # opening the uploaded image
    #     im = Image.open(self.profile_picture)

    #     output = BytesIO()

    #     # resize or modify the image
    #     im = im.resize((10, 10))

    #     # after modification, save it to the output
    #     im.save(output, format='JPEG', quality=10, optimize=True)

    #     output.seek(0)
    #     self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.profile_picture.name.split('.')[0], 'image/jpeg',
    #                                       sys.getsizeof(output), None)

    #     super(Profile, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.id:
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
