from dndmusic.base.exceptions import TaggingException
from dndmusic.base.models.custom_fields import ListOfStringsField
from django.db import models
from typing import List



class Tag(models.Model):
    name=models.CharField(max_length=20)
    objects = models.Manager()
    
    def __str__(self):
        return self.name
    