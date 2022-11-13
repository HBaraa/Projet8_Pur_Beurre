from django import forms


class GetProductForm(forms.Form):
    cherched_product = forms.CharField(label="Produit recherché", max_length=200)


class GetProductChoiceForm(forms.Form):
    chosed_product = forms.CharField(label="produit recherché", max_length=100)
