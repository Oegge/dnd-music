from django.db import models
from dndmusic.base.models.tagging import Description
from pydub import AudioSegment
import datetime

class Song(models.Model):
    name = models.CharField(max_length=50)
    audio = models.FileField(upload_to='audios/')
    duration = models.CharField(max_length=8)
    descriptions = models.ManyToManyField(Description, related_name="songs",null=True,blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._calculate_duration_()

    def give_tag(self, description:Description):
        if self._is_duplicate_tag_(description):
            self._remove_same_tags_(description)
        self.descriptions.append(description)

    def _is_duplicate_tag_(self, description:Description) -> bool:
        tags = {description.get_tag() for description in self.descriptions}
        tag = description.get_tag()
        return tag in tags
    
# --------------------------------------------------------------------------
# private methods:

    def _calculate_duration_(self):
        audio_path = self.audio.path
        audio_segment = AudioSegment.from_file(audio_path)
        duration_in_seconds = int(len(audio_segment) / 1000) 
        duration_obj = datetime.timedelta(seconds=duration_in_seconds)
        self.duration = str(duration_obj)
    
    def _remove_same_tags_(self, description:Description):
        self.descriptions = [item for item in self.descriptions if item.get_tag() != description.get_tag()]
