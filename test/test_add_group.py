# -*- coding: utf-8 -*-



from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="1234", header="5678", footer="90"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))