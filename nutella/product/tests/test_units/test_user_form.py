from django.test import TestCase
from nutella.product.forms import SignUpForm


class CustomUserCreationFormTest(TestCase):

    def test_custom_user_creation_form_email_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['email'].label == None or form.fields['email'].label == 'Email')   # noqa

    def test_custom_user_creation_form_first_name_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['first_name'].label == None or form.fields['first_name'].label == 'First name')   # noqa

    def test_custom_user_creation_form_second_name_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields['second_name'].label == None or form.fields['second_name'].label == 'Second name')  # noqa

    def test_custom_user_creation_form(self):
        form_data = {
            'email': 'remi@purbeurre.com',
            'first_name': 'Remi',
            'second_name': 'PetitChef',
            'password1': 'Some.hi1',
            'password2': 'Some.hi1',
            }

        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())
