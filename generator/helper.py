'''
Created on Oct 30, 2014

@author: rene
'''


class DataObject:

    def __init__(self, name=None, internal_name=None):
        self.name = name
        self.internal_name = internal_name
        self.fields = []


class DataField:

    def __init__(self, name, internal_name, ftype):

        self.attributes = {}
        self.name = name
        self.internal_name = internal_name
        self.is_list = False
        self.ftype = ftype


class ListField():

    def __init__(self, name, internal_name, object_name):
        self.attributes = {}
        self.name = name
        self.internal_name = internal_name
        self.is_list = False
        self.object_name = object_name
