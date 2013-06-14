from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=50)
    target = models.TextField()

    class Meta:
        db_table = 'service'
