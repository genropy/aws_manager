#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage


class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='AWS package', sqlschema='aws',
                    name_short='AWS', name_long='AWS', name_full='AWS')

class Table(GnrDboTable):
    pass
