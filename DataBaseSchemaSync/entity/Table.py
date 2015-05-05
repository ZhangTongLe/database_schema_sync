#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 表实体
class Table(object):
    def __init__(self, name, db):
        # @AttributeType string
        # 表名
        self.__name = name
        # @AssociationType DataBaseSchemaSync.entity.DataBase
        # @AssociationMultiplicity 1
        self.__db = db
        # @AssociationType DataBaseSchemaSync.entity.Field[]
        # @AssociationMultiplicity 0..*
        # @AssociationKind Aggregation
        self.__fields = []

    def get_name(self):
        return self.__name

    def get_db(self):
        return self.__db

    def get_fields(self):
        return self.__fields
