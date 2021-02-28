from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 16)]


class CartAddProductForm(forms.Form):
    """
    Number of products in (Shopping) Cart. Limited to 16 (see above).
    """
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
