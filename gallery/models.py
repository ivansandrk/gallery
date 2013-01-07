from django.db import models
import os, random, string

_charset = string.ascii_lowercase + string.digits

def _generate_filename(instance, old_filename):
    ext = os.path.splitext(old_filename)[1]
    name = ''.join(random.choice(_charset) for i in range(6))
    return 'images/' + name + ext

class Image(models.Model):
    original = models.ImageField(upload_to=_generate_filename)
    description = models.TextField()

class Comment(models.Model):
    image = models.ForeignKey(Image, related_name='comments')
    text  = models.TextField()

