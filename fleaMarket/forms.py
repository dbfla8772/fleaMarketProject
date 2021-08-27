from django import forms
from .models import FleaMarket

class FleaMarketForm(forms.ModelForm): # 장고에서 지원해주는 forms를 상솓받음
    class Meta: 
        model = FleaMarket
        fields = ['title', 'price', 'region', 'lat', 'long', 'category', 'content', 'image', 'file'] 