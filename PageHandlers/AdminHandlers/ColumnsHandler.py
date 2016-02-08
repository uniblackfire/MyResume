import pymongo
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web

from Constants import CURRENT_MONGODB

class ColumnsHandler(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.render('admin/columns.html')




