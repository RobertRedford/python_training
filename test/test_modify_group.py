from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Modify test name"))
    app.group.modify_first_group(Group(name="New group"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="Modify test header"))
    app.group.modify_first_group(Group(header="New header"))

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="Modify test header"))
    app.group.modify_first_group(Group(footer="New footer"))