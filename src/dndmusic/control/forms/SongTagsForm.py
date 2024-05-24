from django import forms

from dndmusic.base.models.song import Song
from dndmusic.base.models.tagging import Tag
from django_select2.forms import Select2MultipleWidget

class SongTagsForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=Select2MultipleWidget(attrs={'class': 'select2'}),
        required=False
    )

    class Meta:
        model = Song
        fields = ['tags']

    def __init__(self, *args, **kwargs):
        super(SongTagsForm, self).__init__(*args, **kwargs)
