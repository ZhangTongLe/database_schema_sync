#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 字段实体
class Field(object):
    def __init__(self, field, types, collation, null, key, default, extra, comment, table):
        # @AttributeType string
        # 字段名
        self.__field = field
        # @AttributeType string
        # 类型
        self.__type = types
        # @AttributeType string
        # 字符集，可以不设置。继承表设置就可以
        self.__collation = collation
        # @AttributeType string
        # 是否可以为空
        self.__null = null
        # @AttributeType string
        # 是否为主键
        self.__key = key
        # @AttributeType string
        # 默认值
        self.__default = default
        # @AttributeType string
        # 额外信息，比如：oncreate onupdate
        self.__extra = extra
        # @AttributeType string
        # 字段注释
        self.__comment = comment
        # @AssociationType DataBaseSchemaSync.entity.Table
        # @AssociationMultiplicity 1
        self.__table = table

    def get_field(self):
        return self.__field

    def get_collation(self):
        return self.__collation

    def get_null(self):
        return self.__null

    def get_key(self):
        return self.__key

    def get_default(self):
        return self.__default

    def get_extra(self):
        return self.__extra

    def get_comment(self):
        return self.__comment

    def get_table(self):
        return self.__table

    def get_field(self):
        return self.__field