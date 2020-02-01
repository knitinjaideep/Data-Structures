#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 05:54:21 2019

@author: nitinkotcherlakota
"""

#Active Directory
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name
    

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")


sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

child.add_user("child_user")
child.add_user("child_user1")
child.add_user("child_user2")

def is_user_in_group(user, group):
    if isinstance(group, str):
        group = eval(group)
    if user == group.get_name():
        return True
    if user in group.get_users():
        return True
    for grp in group.get_groups():
        return is_user_in_group(user,grp)
print("Is child in Parent group? ",is_user_in_group("child",parent)) #True
print("Is Sub child user in parent group? ",is_user_in_group("sub_child_user",parent)) #True
print("Is parent in child group? ",is_user_in_group("parent",child)) #None
print("Entering blank data:", is_user_in_group("",parent)) #None