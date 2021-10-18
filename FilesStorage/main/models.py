import os
from django.db import models
from django.utils import timezone
from .validator import file_size


class File(models.Model):
    file = models.FileField(null=True, blank=True, upload_to='media', validators=[file_size])
    title = models.CharField(max_length=30,default='')
    type = models.CharField(max_length=15)
    size = models.CharField(max_length=20)
    time = models.DateTimeField(default=timezone.now())
    counter = models.IntegerField(default=0)
    details = models.TextField(max_length=1000)

    def __str__(self):
        return os.path.basename(self.file.name)

    def filename(self):
        return os.path.basename(self.file.name)

    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x / 1000, 2)
            ext = ' kb'
        elif x < y * 1000:
            value = round(x / 1000000, 2)
            ext = ' Mb'
        else:
            value = round(x / 1000000000, 2)
            ext = ' Gb'
        return str(value) + ext

    def filetype(self):

        filename = os.path.basename(self.file.name)
        images = ['jpg', 'jpeg', 'png']
        docs = ['pdf', 'docx', 'pptx']
        archives = ['rar', 'zip']
        for image in images:
            if image in filename:
                return "Picture"
        for doc in docs:
            if doc in filename:
                return "Document"
        for archive in archives:
            if archive in filename:
                return "Archive"
        return "Unknown"


