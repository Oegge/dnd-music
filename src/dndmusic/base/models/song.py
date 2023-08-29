from django.db import models
from dndmusic.base.models.tagging import Description

class Song(models.Model):
    name = models.CharField(max_length=50)
    audio = models.FileField(upload_to='audios/')
    descriptions = models.ManyToManyField(Description, related_name="songs")

    def __init__(self) -> None:
        self.descriptions = {}

    def give_tag(self, description:Description):
        if self._is_duplicate_tag_(description):
            self._remove_same_tags_(description)
        self.descriptions.append(description)

    def _is_duplicate_tag_(self, description:Description) -> bool:
        tags = {description.get_tag() for description in self.descriptions}
        tag = description.get_tag()
        return tag in tags
    
    def _remove_same_tags_(self, description:Description):
        self.descriptions = [item for item in self.descriptions if item.get_tag() != description.get_tag()]
