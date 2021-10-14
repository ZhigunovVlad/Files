
from django.db import models
from django.utils import timezone
from .validator import file_size


class File(models.Model):

    title = models.CharField(max_length=30)
    type = models.CharField(max_length=15)
    size = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    file = models.FileField(null=True, blank=True, upload_to='static',validators=[file_size])

    def __str__(self):
        return self.title



