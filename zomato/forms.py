# forms.py
from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search by Location', max_length=100, required=False)
    rate = forms.ChoiceField(
        label='Select Rate',
        choices=[
            ('5', '4.0 - 5.0'),
            ('4', '3.0 - 4.0'),
            ('3', '2.0 - 3.0'),
            ('2', '1.0 - 2.0'),
            ('1', '0.0 - 1.0'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )