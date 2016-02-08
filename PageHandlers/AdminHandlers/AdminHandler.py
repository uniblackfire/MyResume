import pymongo
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web

from Constants import CURRENT_MONGODB

class AdminHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('admin/index.html', user=self.current_user)
