import time

import pymongo
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web

from Constants import *


class ArticleModule(tornado.web.UIModule):
    def render(self, section):
        return self.render_string('modules/article.html', section=section)


class ListArticleHandler(tornado.web.RequestHandler):
    def get(self, current_page):
        if current_page.strip() == '':
            current_page = '1'
        current_page = int(current_page)

        db = CURRENT_MONGODB
        articles = db['articles']
        ############ 添加测试数据
        articles.delete_many({})
        for num in range(1, 326):
            if num % 2 == 0:
                cat = 'ever'
                catname = '偶数'
            else:
                cat = 'odd'
                catname = '奇数'
            if num % 10 == 0:
                cat += '10'
                catname = '偶数 10呗'
            if num % 3 == 0:
                cat += 'odd3'
                catname = '3倍!'
            article_name = 'article' + str(num)
            articles.insert({
                'articleNum'   : num,
                'article_name' : article_name,
                'url'          : get_root_url() + '/article/' + article_name,  #
                'title'        : 'this is title' + str(num),
                'abstract'     : 'abs!!!' + str(num),
                'content'      : '<p><b>TEST~~~!!!</b></p>',
                'thumbnail'    : 'https://www.baidu.com/img/bd_logo1.spng',
                'addDate'      : time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()),
                'viewTimes'    : 0,
                'category_id'  : cat,
                'category_name': catname,
            })
        ############
        total_page = calc_total_page(articles.count(), RESULTS_PER_PAGE)
        if not 0 < current_page <= total_page:
            # TODO: render 404 page
            render_404_page(self)
            # self.finish()#"<html><body>My custom body</body></html>"
            return
        all_articles = articles.find(skip=RESULTS_PER_PAGE * (current_page - 1),
                                     limit=RESULTS_PER_PAGE
                                     ).sort('articleNum', pymongo.DESCENDING)
        art_dict = list()
        for article in all_articles:
            art_dict.append(article)

        page_num_list = get_page_num_list(total_page, current_page)
        self.render('ArticlesList.html',
                    articles=art_dict,
                    page_num_list=page_num_list,
                    current_page=current_page,
                    total_page=total_page,
                    category_name='全部文章',
                    category='')


def calc_total_page(articles_count, result_num_per_page):
    if articles_count % result_num_per_page == 0:
        total_page = articles_count // result_num_per_page
    else:
        total_page = articles_count // result_num_per_page + 1
    return total_page


def get_page_num_list(total_page, current_page):
    if total_page < 10:
        return [i for i in range(1, total_page + 1)]
    else:
        if current_page <= 5:
            return [i for i in range(1, 10 + 1)]
        elif current_page + 5 < total_page:
            return [i for i in range(current_page - 5, current_page + 5 + 1)]
        else:
            return [i for i in range(current_page - 5, total_page + 1)]


def render_404_page(self):
    self.clear()
    self.set_status(404)
    self.render('404.html')
