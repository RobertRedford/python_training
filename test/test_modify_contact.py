from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.fill_the_field_of_credentials(Contact(firstname="Modify test firstname"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname="New firstname"))
    contact = Contact(firstname="Modify test firstname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_lastname(app):
    if app.contact.count_contacts() == 0:
        app.contact.fill_the_field_of_credentials(Contact(lastname="Modify test lastname"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(lastname="New lastname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_address(app):
    if app.contact.count_contacts() == 0:
        app.contact.fill_the_field_of_credentials(Contact(address="Modify test address"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(address="New address"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)