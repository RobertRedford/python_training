from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_contacts() == 0:
        app.contact.fill_the_field_of_credentials(Contact(firstname="test"))
    app.contact.delete_first_contact()