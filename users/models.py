from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        # Check if this is an existing profile being updated
        if self.pk:
            try:
                old_profile = Profile.objects.get(pk=self.pk)
                # Check if the image has changed and it's not the default image
                if old_profile.image and old_profile.image != self.image and old_profile.image.name != 'default.jpg':
                    # Delete the old image file
                    if os.path.isfile(old_profile.image.path):
                        os.remove(old_profile.image.path)
            except Profile.DoesNotExist:
                pass
        
        super().save(*args, **kwargs)
        
        # Resize the new image
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)