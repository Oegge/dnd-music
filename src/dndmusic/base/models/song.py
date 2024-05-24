import os
from django.db import models
from pydub import AudioSegment
import datetime
from django.contrib.auth.models import User

class Song(models.Model):
    name = models.CharField(max_length=50)
    audio = models.FileField(upload_to='audios/')
    duration = models.CharField(max_length=8,null=True,blank=True)
    last_played = models.DateTimeField(null=True, blank=True)
    uploader = models.ForeignKey(User, related_name='uploaded_songs', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', related_name='songs')

    def save(self, *args, **kwargs):
        if self.name:
            base, ext = os.path.splitext(self.name)
            self.name = base
        if not self.duration:
            try:
                self._calculate_duration_()
            except Exception as e:
                print(e)
        super().save(*args, **kwargs)  

# --------------------------------------------------------------------------
# private methods:

    def _calculate_duration_(self):
        audio_path = self.audio.path
        print(self.audio.path)
        audio_segment = AudioSegment.from_file(audio_path)
        duration_in_seconds = int(len(audio_segment) / 1000) 
        duration_obj = datetime.timedelta(seconds=duration_in_seconds)
        self.duration = str(duration_obj)
    
    

    def __str__(self) -> str:
        return self.name