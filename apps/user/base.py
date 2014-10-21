#-*- coding:utf-8 -*-

from apps import base

from setting import (TEMPLATE_PATH as _TEMPLATE_PATH)

class BaseHandler(base.BaseHandler):

    def initialize(self):
        super(BaseHandler,self).initialize()
        self.template_path = _TEMPLATE_PATH


class ListBaseHandler(base.ListBaseHandler):

    def initialize(self):
        super(ListBaseHandler, self).initialize()
        self.template_path = _TEMPLATE_PATH
