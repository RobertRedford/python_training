from model.contact import Contact
from random import randrange


def test_modify_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.fill_the_field_of_credentials(Contact(firstname="Modify test firstname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Modify test firstname")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_lastname(app):
    if app.contact.count_contacts() == 0:
        app.contact.fill_the_field_of_credentials(Contact(lastname="Modify test lastname"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(lastname="Modify test lastname")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_address(app):
    if app.contact.count_contacts() == 0:
        app.contact.fill_the_field_of_credentials(Contact(address="Modify test address"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(address="Modify test address")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)