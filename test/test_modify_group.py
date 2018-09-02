from model.group import Group
from random import randrange


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Modify test name"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="Modify test header"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="New header")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="Modify test header"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(footer="New footer")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)