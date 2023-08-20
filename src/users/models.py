from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from .utils import get_dominant_color

class Profile(models.Model):
    profile_pic = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dominant_color = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)
        domColor = get_dominant_color(pil_img=img)
        self.dominant_color = domColor
        print(domColor)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)


