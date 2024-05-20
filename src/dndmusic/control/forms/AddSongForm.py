from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from dndmusic.base.models.playlist import Playlist
from dndmusic.base.models.song import Song
from django_select2.forms import Select2MultipleWidget

class AddSongForm(forms.ModelForm):
    songs = forms.ModelMultipleChoiceField(
        queryset=Song.objects.all(),
        widget=Select2MultipleWidget
    )
    class Meta:
        model = Playlist
        fields = ['name', 'songs']

    def __init__(self, *args, **kwargs):
        super(AddSongForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Field('name', css_class='input-block-level'),
            Field('songs', css_class='input-block-level'),
            Submit('submit', 'Save')
        )
        print(Song.objects.all())  # This should list all songs in the database
