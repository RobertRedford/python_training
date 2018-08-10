# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.fill_the_field_of_credentials(Contact(firstname="abc", lastname="def", address="ghi"))

def test_add_empty_contact(app):
    app.contact.fill_the_field_of_credentials(Contact(firstname="", lastname="", address=""))
