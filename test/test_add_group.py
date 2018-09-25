# -*- coding: utf-8 -*-

from model.group import Group
import pytest
# from data.groups import constant as testdata


# testdata = [
#     Group(name=name, header=header, footer=footer)
#     for name in ["", random_string("name", 10)]
#     for header in ["", random_string("header", 20)]
#     for footer in ["", random_string("footer", 15)]
# ]


# @pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, json_groups):
    group = json_groups
    with pytest.allure.step('Given a group list'):
        old_groups = app.group.get_group_list()
    with pytest.allure.step('When I add a group %s list' % group):
        app.group.create(group)
    with pytest.allure.step('Then the new group list is equal to the old list with added group'):
        new_groups = app.group.get_group_list()
        assert len(old_groups) + 1 == len(new_groups)
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
