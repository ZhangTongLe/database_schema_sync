#!/usr/bin/python
# -*- coding: UTF-8 -*-
from DataBaseSchemaSync.db.DataBaseConnector import DataBaseConnector
import MySQLdb
from DataBaseSchemaSync.entity.Field import Field
from DataBaseSchemaSync.entity.Table import Table
from DataBaseSchemaSync.entity.DataBase import DataBase
import json

TIME_OUT = 10  # 10 seconds


# Mysql实现
class MysqlDataBaseConnector(DataBaseConnector):
    def __init__(self, config):
        self.database = DataBase(config['database'])
        self.__db = MySQLdb.connect(host=config['ip'], user=config['userName'], passwd=config['password'], db=config['database'], connect_timeout=TIME_OUT)
        self.__cursor = self.__db.cursor()

    # 查询字段
    # @ReturnType DataBaseSchemaSync.entity.Field
    def fetch_fields(self):
        tables = self.database.get_tables()

        for i in tables:
            fields = self.query_fields(i.get_name())

            for f in fields:
                field = Field(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[8], i)
                i.get_fields().append(field)

    # 查询字段
    # @ParamType table string
    # 表名
    # @ReturnType DataBaseSchemaSync.entity.Field
    def query_fields(self, table):
        self.__cursor.execute('''SHOW FULL COLUMNS FROM %s''' % table)
        return self.__cursor.fetchall()

    # 查询数据库表
    # @ReturnType DataBaseSchemaSync.entity.Table
    def fetch_tables(self):
        self.__cursor.execute('''SHOW TABLES''')
        tables = self.__cursor.fetchall()

        for i in tables:
            tb = Table(i[0], self.database)
            self.database.get_tables().append(tb)

    def query_create_table_statement(self, table):
        self.__cursor.execute('''SHOW CREATE TABLE %s''' % table)
        rs = self.__cursor.fetchall()
        return rs

    def create_table(self, statement):
        self.__cursor.execute(statement)

    # 根据对比结果执行同步更新
    # @ParamType diff DataBaseSchemaSync.entity.Diff
    # 对比结果
    # @ReturnType boolean
    def sync(self, diff):
        super(MysqlDataBaseConnector, self).sync(diff)

    def fetch(self):
        self.fetch_tables()
        self.fetch_fields()

    def create_field(self, field):
        # '''ALTER TABLE %s ADD %s %s '''

        pass
