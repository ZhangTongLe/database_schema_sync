#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 数据库中表，及表结构的对比
import sys
from DataBaseSchemaSync.entity.Field import Field
from DataBaseSchemaSync.entity.Diff import Diff
from DataBaseSchemaSync.entity.Field_Diff import FieldDiff
from DataBaseSchemaSync.entity.TableDiff import TableDiff


class SchemaComparison(object):
    # 对比主库与从库的表结果
    # @ParamType main DataBaseSchemaSync.entity.DataBase
    # 主库
    # @ParamType target DataBaseSchemaSync.entity.DataBase
    # 目标库
    # @ReturnType DataBaseSchemaSync.entity.Diff
    def compare(self, source, target):
        diffs = []
        sb = source.get_tables()  # 源表
        tb = target.get_tables()  # 目标表

        sbd = self.__table_to_dict(sb)  # 字典形式
        tbd = self.__table_to_dict(tb)  # 字典形式

        if len(sb) == len(tb):
            for i in sbd.keys():
                try:
                    tbd[i]
                except KeyError as k:
                    sys.stderr.write('table : (%s) does not find in the target database' % k.message)
                    diffs.append(TableDiff(sbd[k.message]), None, Diff.TYPE_LACK)
                    continue

                sfd = self.__field_to_dict(sbd[i].get_fields())  # 字段
                tfd = self.__field_to_dict(tbd[i].get_fields())  # 字段

                for j in sfd.keys():
                    try:
                        tfd[j]
                    except KeyError as k:
                        sys.stderr.write('field : (%s) does not find in the table (%s)' % (k.message, i))
                        diffs.append(FieldDiff(sfd[j], tfd[j], Diff.TYPE_LACK))
                        pass

                    rs = self.__field_compare(sfd[j], tfd[j])
                    if rs != Diff.NONE:
                        diffs.append(FieldDiff(sfd[j], tfd[j], Diff.TYPE_DIFF, where=rs))
            return diffs

        if len(sb) > len(tb):
            print '>'

        if len(sb) < len(tb):
            print '<'

    def __init__(self, source, target):
        self.source = source
        self.target = target

    def __field_compare(self, one, two):
        if one.get_collation() != two.get_collation():
            return Diff.COLLATION

        if one.get_null() != two.get_null():
            return Diff.NULL

        if one.get_key() != two.get_key():
            return Diff.KEY

        if one.get_default() != two.get_default():
            return Diff.DEFAULT

        if one.get_extra() != two.get_extra():
            return Diff.EXTRA

        if one.get_comment() != two.get_comment():
            return Diff.COMMENT

        return Diff.NONE

    def __table_to_dict(self, tables):
        d = {}
        for i in tables:
            d[i.get_name()] = i

        return d

    def __field_to_dict(self, fields):
        d = {}

        for i in fields:
            d[i.get_field()] = i

        return d

    def sync(self, diffs):
        for i in diffs:
            if type(i) == 'Field_Diff':
                self.__sync_field(i)
            else:
                self.__sync_table(i)

    def __sync_table(self, diff):
        rs = self.source.query_create_table_statement(diff.where)
        self.target.create_table(rs[0][1])

    def __sync_field(self, diff):
        # 目标库缺少此字段，直接在目标库表中创建即可
        if diff.diff_type == Diff.TYPE_FIELD_NONE:
            pass

        # 字符编码
        if diff.where & Diff.COLLATION == Diff.COLLATION:
            pass

        # 字段类型
        if diff.where & Diff.TYPE == Diff.TYPE:
            pass

        # 是否可以为空
        if diff.where & Diff.NULL == Diff.NULL:
            pass

        # 是否为主键
        if diff.where & Diff.KEY == Diff.KEY:
            pass

        # 默认值
        if diff.where & Diff.DEFAULT == Diff.DEFAULT:
            pass

        # 额外字段如：ONUPDATE
        if diff.where & Diff.EXTRA == Diff.EXTRA:
            pass

        # 备注
        if diff.where & Diff.COMMENT == Diff.COMMENT:
            pass