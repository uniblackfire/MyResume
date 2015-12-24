import pymongo
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web

from Constants import CURRENT_MONGODB

class AdminSigninHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/signin.html')