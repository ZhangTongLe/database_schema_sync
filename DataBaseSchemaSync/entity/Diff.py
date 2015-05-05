#!/usr/bin/python
# -*- coding: UTF-8 -*-
from DataBaseSchemaSync.entity import Field


# 对比结果
class Diff(object):

    TYPE = 1 << 0
    COLLATION = 1 << 1
    NULL = 1 << 2
    KEY = 1 << 3
    DEFAULT = 1 << 4
    EXTRA = 1 << 5
    COMMENT = 1 << 6
    NONE = 0

    TYPE_TABLE = 1
    TYPE_FIELD = 2
    TYPE_FIELD_NONE = 3

    def __init__(self, source, target, diff_type=TYPE_FIELD, value=None):
        self.where = value
        self.diff_type = diff_type

        # @AttributeType DataBaseSchemaSync.entity.Field
        # 源数据库
        self.__sourceField = source
        # @AttributeType DataBaseSchemaSync.entity.Field
        # 目标字段
        self.__targetField = target

        if self.diff_type == Diff.TYPE_FIELD:
            if value is None:
                self.where = Diff.NONE
            else:
                self.where = value

    def get_source_field(self):
        return self.__sourceField

    def get_target_field(self):
        return self.__targetField
