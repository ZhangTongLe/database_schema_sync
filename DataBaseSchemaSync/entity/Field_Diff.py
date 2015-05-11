#!/usr/bin/python
# -*- coding: UTF-8 -*-
from DataBaseSchemaSync.entity import Diff


# 字段差异类
class FieldDiff(Diff):
    def __init__(self, src, dst, diff_type, where=None):
        # @AttributeType DataBaseSchemaSync.entity.Field
        # 源
        self.src = src
        # @AttributeType DataBaseSchemaSync.entity.Field
        # 目标
        self.dst = dst
        # @AttributeType str
        # 目标
        self.diff_type = diff_type
        # @AttributeType int
        # 位置
        self.where = where

