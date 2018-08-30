# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="1234", lastname="5678", address="90")
    app.contact.fill_the_field_of_credentials(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)

def test_add_empty_contact(app):
    app.contact.fill_the_field_of_credentials(Contact(firstname="", lastname="", address=""))