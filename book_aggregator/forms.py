from django import forms
from book_aggregator.models import Book


# class BookForm(forms.Form):
#     sources = forms.ChoiceField(
#         widget=forms.Select(),
#         choices=[],
#         required=False
#     )


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control mb-1", 'placeholder': 'Enter search term...'}),
        required=False)


class MulttipleData(forms.MultipleChoiceField):
    def create_option(
            self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        div = super().create_option(
            name, value, label, selected, index, subindex, attrs
        )
        div["attrs"]["class"] = 'list-group-item'
        return div


class SortForm(forms.Form):
    CHOICES = [
        ('default', 'По умолчанию'),
        ('increase_price', 'По возрастанию цены'),
        ('decrease_price', 'По убыванию цены'),
    ]
    sort = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-select',
                'style': 'max-width: 260px;'
            }
        ),
        choices=CHOICES,
        required=False
    )


class FilterForm(forms.Form):
    authors = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        # attrs={'class': "form-select", 'size': "3", 'aria-label': "size 3 select example"}),
        # attrs={"class": "form-check-input me-1"}),
        # choices=authors_choices,
        choices=[],
        required=False
    )
    genre = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple(),
        # attrs={'class': "form-select", 'size': "3", 'aria-label': "size 3 select example"}),
        # attrs={"class": "form-check-input me-1"}),
        # choices=authors_choices,
        choices=[],
        required=False
    )
    more_than_four = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input'}
        ),
        required=False
    )
    have_electronic = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input'}
        ),
        required=False
    )
    have_physical = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input'}
        ),
        required=False
    )

    # def __init__(self, *args, **kwargs):
    #     authors_choices = kwargs.pop('authors_choices', [])
    #     super().__init__(*args, **kwargs)
    #     self.fields['authors'].choices = authors_choices
    # price = f
    # price_from = forms.DecimalField(
    #     widget=forms.NumberInput(
    #         attrs={
    #             'class': 'input-group mt-2',
    #             'style': 'max-width: auto; padding: 5px;',
    #             'placeholder': 'От',
    #         }
    #     ),
    #     required=False
    # )
    # price_to = forms.DecimalField(
    #     widget=forms.NumberInput(
    #         attrs={
    #             'class': 'input-group mt-2 ms-2 me-2',
    #             'style': 'max-width: auto; padding: 5px;',
    #             'placeholder': 'До',
    #         }
    #     ),
    #     required=False
    # )
