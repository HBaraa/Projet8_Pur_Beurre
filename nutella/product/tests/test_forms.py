from django.test import TestCase
from nutella.product.forms import SignUpForm


class TestSignUpForm(TestCase):
    def test_custom_user_creation_form_email_field_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields["email"].label == "Email")

    def test_custom_user_creation_form_first_name_field_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields["first_name"].label == "First name")

    def test_custom_user_creation_form_second_name_field_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields["second_name"].label == "Second name")

    def test_custom_user_creation_form_password1_field_label(self):
        form = SignUpForm()
        self.assertTrue(form.fields["password1"].label == "Mot de passe")

    def test_custom_user_creation_form_password2_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields["password2"].label == "Confirmation du mot de passe"
        )

    def test_custom_user_creation_form(self):
        form_data = {
            "email": "colettebaraa@purbeurre.com",
            "first_name": "baraa",
            "second_name": "colette",
            "password1": "sfsfsfff.4",
            "password2": "sfsfsfff.4",
        }

        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())
