from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    #title = forms.CharField(max_length=50)
   #slug = forms.CharField(max_length=50)
    #title.widget.attrs.update({'class': 'form-control'})
    #slug.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title':forms.TextInput(attrs={'class': 'form-control'}),
                   'slug':forms.TextInput(attrs={'class': 'form-control'}),
                   }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('slug may not be "create"')

        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'text', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

        def clean_slug(self):
            new_slug=self.cleaned_data['slug'].lower()
            if new_slug == 'create':
                raise ValidationError('slug may not be "create"')