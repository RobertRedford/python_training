# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_the_field_of_credentials(Contact(firstname="abc", lastname="def", address="ghi"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_the_field_of_credentials(Contact(firstname="", lastname="", address=""))
    app.session.logout()
