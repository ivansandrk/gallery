from django import forms
from gallery.models import Image, Comment

class ImageForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['original'].label = 'Odaberi sliku'
        self.fields['description'].label = 'Opis slike'
        self.fields['description'].widget = forms.TextInput()
        
    class Meta:
        model = Image

class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        foreign_key = kwargs.pop('foreign_key')
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget = forms.HiddenInput()
        self.fields['image'].initial = foreign_key
        self.fields['text'].label = ''
        self.fields['text'].widget.attrs['cols'] = 70
        self.fields['text'].widget.attrs['rows'] = 6
    
    class Meta:
        model = Comment

