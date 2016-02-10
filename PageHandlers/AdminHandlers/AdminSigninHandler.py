import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("username")


class AdminSigninHandler(BaseHandler):
    def get(self):
        self.render('admin/signin.html')

    def post(self):
        print(self.get_argument("username"))
        self.set_secure_cookie("username", self.get_argument("username"))
        self.redirect(self.get_argument('next', '/admin'))


class AdminSignoutHandler(BaseHandler):
    def get(self):
        if self.get_argument("logout", None):
            self.clear_cookie("username")
            self.redirect("/")
