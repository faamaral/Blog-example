from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post


class Postform(forms.ModelForm):
    #title = forms.CharField(max_length=100)
    content = forms.CharField(widget=CKEditorUploadingWidget())
    sumary = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        #fields = '__all__'
        fields = ('title', 'sumary','content', 'category', 'image', 'status')
