#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 数据库实体
class DataBase(object):
    def __init__(self, name):
        # @AttributeType string
        # 数据库名
        self.__name = None
        # @AssociationType DataBaseSchemaSync.entity.Table[]
        # @AssociationMultiplicity 0..*
        # @AssociationKind Aggregation
        self.__tables = []

    def get_name(self):
        return self.__name

    def get_tables(self):
        return self.__tables

