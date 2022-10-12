from django.db import models


class something(models.Model):
    
    first = models.CharField(max_length=200)
    second = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first