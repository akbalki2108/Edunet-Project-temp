# forms.py
from django import forms

class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search by Location', max_length=100, required=False)
    rate = forms.ChoiceField(
        label='Select Rate',
        choices=[
            (0, 'None'),
            (5, '4.0 - 5.0'),
            (4, '3.0 - 4.0'),
            (3, '2.0 - 3.0'),
            (2, '1.0 - 2.0'),
            (1, '0.0 - 1.0'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    online_order = forms.ChoiceField(
        label='Select online order',
        choices=[
            (0, 'None'),
            (1, 'Yes'),
            (2, 'No'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    book_table = forms.ChoiceField(
        label='Select book table',
        choices=[
            (0, 'None'),
            (1, 'Yes'),
            (2, 'No'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    listed_in_type = forms.ChoiceField(
        label='Select Type',
        choices=[
            (None, 'None'),
            ("Buffet", 'Buffet'),
            ("Delivery", 'Delivery'),
            ("Dine-out", 'Dine-out'),
            ("Desserts", 'Desserts'),
            ("Cafes", 'Cafes'),
            ("Drinks & nightlife", 'Drinks & nightlife'),
            ("Pubs and bars", 'Pubs and bars'),
        ],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )