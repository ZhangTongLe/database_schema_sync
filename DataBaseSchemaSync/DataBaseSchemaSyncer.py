#!/usr/bin/python
# -*- coding: UTF-8 -*-
from _mysql import OperationalError
import sys
import os
from DataBaseSchemaSync.SchemaComparison import SchemaComparison

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from DataBaseSchemaSync.db.MysqlDataBaseConnector import MysqlDataBaseConnector
import json
from DataBaseSchemaSync.util.configer import Configer


class DataBaseSchemaSyncer(object):
    def __init__(self):
        try:
            configure = Configer()
        except IOError:
            sys.stderr.write('file not exist')
            sys.exit(1)

        self.db = json.loads(configure.get_config())

        try:
            self.source = MysqlDataBaseConnector(self.db['source'])
        except OperationalError:
            sys.stderr.write('database connect error')
            sys.exit(1)

        try:
            self.target = MysqlDataBaseConnector(self.db['target'])
        except OperationalError:
            sys.stderr.write('database connect error')
            sys.exit(1)

        self.source.fetch()
        self.target.fetch()
        self.compare()

    def compare(self):
        cmp = SchemaComparison(self.source, self.target)
        diffs = cmp.compare(self.source.database, self.target.database)
        cmp.sync(diffs)


if __name__ == "__main__":
    DataBaseSchemaSyncer()


