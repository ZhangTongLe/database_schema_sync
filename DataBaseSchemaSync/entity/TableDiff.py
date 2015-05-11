#!/usr/bin/python
# -*- coding: UTF-8 -*-
from DataBaseSchemaSync.entity import Diff


# 表差异
class TableDiff(Diff):
    def __init__(self, src, dst, diff_type):
        # @AttributeType DataBaseSchemaSync.entity.Table
        # 源
        self.src = src
        # @AttributeType DataBaseSchemaSync.entity.Table
        # 目标
        self.dst = dst
        # @AttributeType DataBaseSchemaSync.entity.Table
        # 目标
        self.diff_type = diff_type


