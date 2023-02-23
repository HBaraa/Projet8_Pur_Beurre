from django.test import TestCase
from nutella.product.forms import SignUpForm
from nutella.product.models import CustomUser


class TestSignUpForm(TestCase):
    def test_custom_user_creation_form_email_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields["email"].label == None
            or form.fields["email"].label == "Email"
        )

    def test_custom_user_creation_form_first_name_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields["first_name"].label == None
            or form.fields["first_name"].label == "First name"
        )

    def test_custom_user_creation_form_second_name_field_label(self):
        form = SignUpForm()
        self.assertTrue(
            form.fields["second_name"].label == None
            or form.fields["second_name"].label == "Second name"
        )

    def test_custom_user_creation_form(self):
        form_data = {
            "email": "colettebaraa@purbeurre.com",
            "first_name": "baraa",
            "last_name": "colette",
            "password1": "sfsfsfff.4",
            "password2": "sfsfsfff.4",
        }

        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_with_false_email(self):
        form_data = {
            "email": "colettebaraa",
            "first_name": "baraa",
            "last_name": "colette",
            "password1": "sfsfsfff.4",
            "password2": "sfsfsfff.4",
        }

        form = SignUpForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.error_messages)

    def test_custom_user_with_false_password2(self):
        form_data = {
            "email": "colettebaraa@purbeurre.com",
            "first_name": "baraa",
            "last_name": "colette",
            "password1": "sfsfsfff.4",
            "password2": "sfsfgxffd4",
        }

        form = SignUpForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.error_messages)

    def test_custom_user_without_first_name(self):
        form_data = {
            "email": "colettebaraa@purbeurre.com",
            "first_name": "",
            "last_name": "colette",
            "password1": "sfsfsfff.4",
            "password2": "sfsfsfff.4",
        }

        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_without_last_name(self):
        form_data = {
            "email": "colettebaraa@purbeurre.com",
            "first_name": "baraa",
            "last_name": "",
            "password1": "sfsfsfff.4",
            "password2": "sfsfsfff.4",
        }

        form = SignUpForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_existing_user(self):
        customer1 = CustomUser.objects.create_user(       # noqa
            email="colette@purbeurre.com",
            first_name="colette",
            second_name="purbeurre",
            password="kjhkhfkh5",
        )
        customer2 = {
            "email": "colette@purbeurre.com",
            "first_name": "colette",
            "last_name": "purbeurre",
            "password1": "hngghgjgcg6",
            "password2": "hngghgjgcg6",
        }

        form = SignUpForm(data=customer2)
        print(form.errors)
        self.assertTrue(form.error_messages)

