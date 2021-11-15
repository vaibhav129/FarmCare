from django import forms
from .models import Auction

class uploads(forms.ModelForm):
    class Meta:
        model = Auction
        fields = ('title', 'image' , 'bid' , 'describe', 'category')