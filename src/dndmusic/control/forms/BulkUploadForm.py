from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from dndmusic.control.forms.MultipleFileInput import MultipleFileField


class BulkUploadForm(forms.Form):
    audio_files = MultipleFileField(help_text="Select multiple files")

    def __init__(self, *args, **kwargs):
        super(BulkUploadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        # Define the layout
        self.helper.layout = Layout(
            Field('audio_files', css_class='input-group-lg'),
            Submit('submit', 'Upload', css_class='btn-primary')
        )
