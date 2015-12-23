import pymongo
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web

from Constants import *
from PageHandlers.ListArticleHandler import calc_total_page, get_page_num_list, render_404_page


class CategoryHandler(tornado.web.RequestHandler):
    def get(self, category, current_page):
        if current_page.strip() == '':
            current_page = '1'
        current_page = int(current_page)

        db = CURRENT_MONGODB
        articles = db['articles']

        cat_articles = articles.find({'category_id': category},
                                     skip=RESULTS_PER_PAGE * (current_page - 1),
                                     limit=RESULTS_PER_PAGE
                                     ).sort('articleNum', pymongo.DESCENDING)

        total_page = calc_total_page(cat_articles.count(), RESULTS_PER_PAGE)
        if not 0 < current_page <= total_page:
            # TODO: render 404 page
            render_404_page(self)
            # self.finish()#"<html><body>My custom body</body></html>"
            return

        art_dict = list()
        for article in cat_articles:
            art_dict.append(article)

        page_num_list = get_page_num_list(total_page, current_page)
        self.render('ArticlesList.html',
                    articles=art_dict,
                    page_num_list=page_num_list,
                    current_page=current_page,
                    total_page=total_page,
                    category_name=get_category_name_by_id(category),
                    category=get_root_url() + '/category/' + category + '/')
