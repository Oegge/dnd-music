from dndmusic.base.exceptions import TaggingException
from dndmusic.base.models.custom_fields import ListOfStringsField
from django.db import models
from typing import List

class Scale(models.Model):
    name = models.CharField(max_length=50)
    values = ListOfStringsField()
    def __init__(self, name:str, values:List[str]) -> None:
        self.name = name
        self.values = values

    def is_valid_value(self, value:str):
        return value in self.values


class Tag(models.Model):
    name=models.CharField(max_length=20)
    scale=models.ForeignKey(Scale, null=True)
    def __init__(self, name:str, scale:Scale) -> None:
        self.name = name
        self.scale = scale
    
    def is_valid_value(self, value:str):
        if self.scale is None:
            return False
        return self.scale.is_valid_value(value)


class Description(models.Model):
    tag = models.ForeignKey(Tag, related_name="descriptions")
    value = models.CharField(max_length=20, null=True)
    def __init__(self, tag:Tag, value:str) -> None:
        self.tag = tag
        if tag.is_valid_value(value):
            self.value = value
        else: raise TaggingException("Incorrect value for this type of tag")
    
    def get_tag(self) -> Tag:
        return self.tag