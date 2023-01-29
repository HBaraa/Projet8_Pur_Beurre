from django.test import TestCase
from nutella.product.forms import GetProductChoiceForm, GetProductForm


class GetProductChoiceFormTest(TestCase):
    '''
    Tests the Product Choice form.
    '''

    def test_cherched_product_field_label(self):
        form = GetProductChoiceForm()
        self.assertTrue(
            form.fields['chosed_product'].label == None or form.fields['chosed_product'].label == 'produit recherché')

    def test_get_product_choice_form(self):
        form_data = {'chosed_product': 'something'}
        form = GetProductChoiceForm(data=form_data)
        self.assertTrue(form.is_valid())


class GetProductFormTest(TestCase):
    '''
    Tests the Get Product form.
    '''
    def test_cherched_product_field_label(self):
        form = GetProductForm()
        self.assertTrue(
            form.fields['cherched_product'].label == None or form.fields['cherched_product'].label == 'Produit recherché')  # noqa

    def test_get_product_form(self):
        form_data = {'cherched_product': 'something'}
        form = GetProductForm(data=form_data)
        self.assertTrue(form.is_valid())
