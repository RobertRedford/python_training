from model.contact import Contact


def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Contact(firstname="New firstname"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_contact(Contact(lastname="New lastname"))
    app.session.logout()

def test_modify_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.modify_first_group(Contact(address="New address"))
    app.session.logout()