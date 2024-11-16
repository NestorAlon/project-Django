from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        multiple_check_box_data = [
        ('one', 'item 1'),
        ('two', 'item 2'),
        ('three', 'item 3'),
        ('four', 'item 4'),
        ('five', 'item 5'),
        ]
        
        pulldown_data = [
            ('1', 'choice 1'),
            ('2', 'choice 2'),
            ('3', 'choice 3'),
        ]
        
        radio_data = [
            ('data 1', 'radio 1'),
            ('data 2', 'radio 2'),
            ('data 3', 'radio 3'),
        ]
        
        widgets = {
            'check_box': forms.CheckboxInput(),
            'multiple_check_box': forms.CheckboxSelectMultiple(choices=multiple_check_box_data),
            'pulldown': forms.Select(choices=pulldown_data),
            'radio': forms.RadioSelect(choices=radio_data),
        }