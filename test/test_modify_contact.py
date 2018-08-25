from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count_contacts() == 0:
        app.contact.fill_the_field_of_credentials(Contact(firstname="Modify test firstname"))
    app.contact.modify_first_contact(Contact(firstname="New firstname"))

def test_modify_contact_lastname(app):
    if app.contact.count_contacts() == 0:
        app.contact.fill_the_field_of_credentials(Contact(lastname="Modify test lastname"))
    app.contact.modify_first_contact(Contact(lastname="New lastname"))

def test_modify_contact_address(app):
    if app.contact.count_contacts() == 0:
        app.contact.fill_the_field_of_credentials(Contact(address="Modify test address"))
    app.contact.modify_first_contact(Contact(address="New address"))