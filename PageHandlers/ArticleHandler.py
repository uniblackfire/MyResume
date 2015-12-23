import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web

from Constants import *


class ArticleHandler(tornado.web.RequestHandler):
    def get(self, article_name):
        if article_name:
            db = CURRENT_MONGODB
            articles = db['articles']
            display_article = articles.find_one({'article_name': article_name})

        self.render('ArticleContent.html',
                    article=display_article)
