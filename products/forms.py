from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'is_subscription', 'duration_days']

    def clean(self):
        cleaned_data = super().clean()
        is_sub = cleaned_data.get('is_subscription')
        duration = cleaned_data.get('duration_days')

        if is_sub and not duration:
            self.add_error('duration_days', 'Enter duration for subscription product')
        elif not is_sub:
            cleaned_data['duration_days'] = None

        return cleaned_data
