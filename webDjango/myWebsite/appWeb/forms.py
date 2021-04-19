from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'content', 'email', 'time_create'}
        widget = {
            'title' : forms.TextInput(attrs={'class':'testTitleClass'}),
            'content' : forms.Textarea(attrs={'class':'testContentClass', 'id':'IDcontent'})
        }


class SendEmail(forms.Form):
    # dung widget cho viec css giao dien
    title = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'testClassTitle'}))
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'testClassContent', 'id':'contentID'}))
    cc = forms.BooleanField(required=False)
