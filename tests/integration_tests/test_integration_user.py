from django.urls import reverse, resolve
from django.test import Client
from django.contrib import auth

from nutella.product.views import signup, logout_view, moncompte
from nutella.product.forms import SignUpForm

import pytest
from pytest_django.asserts import assertTemplateUsed


CLIENT = Client()


@pytest.mark.django_db
def test_login_route():

    """
    First we test if the 'login' route maps to 'LoginView',
    then we check if the LoginView
    renders the correct template ( registration/login.html )
    Then, we create a temporary user, and login with
    those credentials and see whether user
    is redirected to '/home/' route if the login was successful
    """

    credentials = {
        'email': 'testuser@testing.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    temp_user = CLIENT.post(reverse('signup'), credentials)                                                                                                                                                                                                                                                               # noqa
    response = CLIENT.post(reverse('login'), {'username': 'testuser@testing.com', 'password': 'TestPassword'})                                                                                                                                                                                        # noqa
    assert response.status_code == 302
    assert response.url == reverse('home')

    user = auth.get_user(CLIENT)
    assert user.is_authenticated


@pytest.mark.django_db
def test_login_route_failed_wrong_password():

    """
    Testing if the user enters the false password
    then the user stays on the 'login' route,
    """
    response = CLIENT.post(reverse('login'), {'username': 'testuser@testing.com', 'password': 'WrongPassword'})                                                                                                                                                         # noqa
    assertTemplateUsed(response, 'accounts/login.html')


@pytest.mark.django_db
def test_login_route_failed_wrong_username():

    """
    Testing if the user enters the false username
    then the user stays on the 'login' route,
    and is asked to re-enter the correct username
    """

    response = CLIENT.post(reverse('login'), {'username': 'WrongUsernam', 'password': 'TestPassword'})                                                                                                                                                      # noqa
    assertTemplateUsed(response, 'accounts/login.html')


@pytest.mark.django_db
def test_login_route_failed():

    """
    Testing if the user enters the false credentails
    then the user stays on the 'login' route,
    and is asked to re-enter the correct credentials
    """

    response = CLIENT.post(reverse('login'), {'username': 'WrongUsername', 'password': 'WrongPassword'})     # noqa
    assertTemplateUsed(response, 'accounts/login.html')


@pytest.mark.django_db
def test_signup_route():

    """
    Test approach starts with testing if the 'signup'
    route maps to 'SignUpView'. Then we test
    if the SignUpView renders the correct template
    ( signup.html ) with correct Form ( SignUpForm ).
    After that we create a temporary user, by using our
    'signup' route and checking if redirects the user to
    the 'login' route, if everything went fine.
    """

    # Testing if the 'signup' route maps to 'SignUpView'
    url = reverse('signup')
    assert resolve(url).func, signup

    """ Testing if the SignUpView renders the correct template
    ( registration/signup.html ) with correct Form ( SignupForm )"""
    response = CLIENT.get(reverse('signup'))
    assert response.status_code == 200
    assert SignUpForm.is_valid
    assertTemplateUsed(response, 'signup.html')

    credentials = {
        'email': 'testuser@testing.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    """ creating a temporary user and testing if the user
    gets redirected to 'home' route if signup was successful"""
    response = CLIENT.post(reverse('signup'), credentials)
    assert response.status_code == 302
    assert response.url == reverse('home')


@pytest.mark.django_db
def test_signup_route_failed():

    """
    Testing 'signup' route with the wrong credentials
    and testing if user stays on the 'signup'
    route if the signup process failed
    """

    credentials = {
        'email': 'testuser@testing.com',
        'first_name': 'Test',
        'last_name': 'User',
        'password1': '',  # password not matching
        'password2': 'TestPassword'
    }
    response = CLIENT.post(reverse('signup'), credentials)
    assertTemplateUsed(response, 'signup.html')


@pytest.mark.django_db
def test_logout_route():

    """
    First we test if 'logout' route maps to the 'LogoutView' or not,
    then we test if the user is
    properly logged out and is redirected to 'home' route
    """

    # Testing if the 'logout' route maps to 'LogoutView'
    url = reverse('logout')
    assert resolve(url).func, logout_view

    # Testing if the user is logged out properly and is redirected to 'home'
    response = CLIENT.get(reverse('logout'))                        # noqa
    assert response.status_code == 302
    assert response.url == reverse('home')


@pytest.mark.django_db
def test_profile_route():

    """
    First we test if 'profile' route  maps to 'ProfileView',
    then we login with a temporary user and
    access the profile route and test if the
    correct template ( profile.html ) was rendered
    """

    # Testing if the 'profile' route maps to 'ProfileView'
    url = reverse('moncompte')
    assert resolve(url).func, moncompte

    credentials = {
        'first_name': 'Test',
        'last_name': 'User',
        'email': 'testuser@testing.com',
        'password1': 'TestPassword',
        'password2': 'TestPassword'
    }
    temp_user = CLIENT.post(reverse('signup'), credentials)                  # noqa
    CLIENT.post(reverse('login'), {'username': 'testuser@testing.com', 'password': 'TestPassword'})      # noqa

    # Testing if the ProfileView renders correct template ( profile.html )
    response = CLIENT.get(reverse('moncompte'))                 # noqa
    assert response.status_code == 200
    assertTemplateUsed(response, 'moncompte.html')


@pytest.mark.django_db
def test_profile_route_failed():

    """
    Testing if the user is redirected to 'login' route if the user
    is not authenticated and is
    trying to access the profile
    """
    response = CLIENT.get(reverse('moncompte'))                     # noqa
    assert response.status_code == 302
