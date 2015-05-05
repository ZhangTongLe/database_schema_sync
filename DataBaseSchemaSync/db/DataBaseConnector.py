#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 数据库连接
class DataBaseConnector(object):
    # 查询数据库表
    # @ReturnType DataBaseSchemaSync.entity.Table
    def query_tables(self):
        pass

    # 查询字段
    # @ParamType table string
    # 表名
    # @ReturnType DataBaseSchemaSync.entity.Field
    def query_fields(self, table):
        pass

    # 根据对比结果执行同步更新
    # @ParamType diff DataBaseSchemaSync.entity.Diff
    # 对比结果
    # @ReturnType boolean
    def sync(self, diff):
        pass

    def __init__(self):
        pass

