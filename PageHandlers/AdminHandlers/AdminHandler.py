import pymongo
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web

from Constants import CURRENT_MONGODB
from PageHandlers.AdminHandlers.AdminSigninHandler import BaseHandler


class AdminHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('admin/index.html', user=self.current_user, navi_active_num=0)
