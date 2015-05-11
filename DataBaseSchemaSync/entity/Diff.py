#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 对比结果


class Diff(object):
    TYPE_LACK = 'lack'  # 字段或者表不存在于目标库中
    TYPE_DIFF = 'diff'  # 字段或者表存在，但是配置有所不同

    TYPE = 1 << 0
    COLLATION = 1 << 1
    NULL = 1 << 2
    KEY = 1 << 3
    DEFAULT = 1 << 4
    EXTRA = 1 << 5
    COMMENT = 1 << 6
    NONE = 0

    def __init__(self):
        # 差异类型：缺失|配置
        self.diff_type = None

