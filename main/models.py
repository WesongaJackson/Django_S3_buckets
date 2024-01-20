import os.path
import uuid

from django.core.files.storage import default_storage
from django.db import models
from PIL import Image


# Create your models here.
def unique_image_name(instance, filename):
    ext = filename.split(".")[-1]
    name = uuid.uuid4()
    fullname = f"{name}.{ext}"
    return os.path.join('images', fullname)


class UploadImage(models.Model):
    image = models.ImageField(upload_to=unique_image_name)
    created_at=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(UploadImage, self).save(*args, **kwargs)
        with default_storage.open(self.image.name) as file:
            img = Image.open(file)
            if img.height > 400 or img.width > 400:
                output_size = (400, 400)
                img.thumbnail(output_size)
                with default_storage.open(self.image.name, 'wb') as new_file:
                    img.save(new_file, format=img.format)
