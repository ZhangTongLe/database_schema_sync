#!/usr/bin/python
# -*- coding: UTF-8 -*-

CONFIG_FILE_PATH = '/tmp/db.json'


# 用于读取数据库配置文件，初始化时调用。
class Configer(object):
    def __init__(self):
        of = open(CONFIG_FILE_PATH)
        self.__config = of.read()

    def get_config(self):
        return self.__config


if __name__ == "__main__":
    Configer()