import pymongo
import tornado.auth
import tornado.httpserver
import tornado.ioloop
import tornado.web

import Constants


class SectionModule(tornado.web.UIModule):
    def render(self, section):
        return self.render_string('modules/section.html', section=section)


class MainHandler(tornado.web.RequestHandler):
    def get(self, current_page):
        # TODO: read sections from MongoDB
        db = Constants.CURRENT_MONGODB
        table = db['sections']
        #############
        table.delete_many({})

        sections = [
            {'num': 1, 'name': 'About', 'id': 'one', 'content': """
             <header class="major">
                    <h2>Read Only</h2>

                    <p>Just an incredibly simple responsive site<br/>
                        template freebie by <a href="http://html5up.net">HTML5 UP</a>.</p>
                </header>
                <p>Faucibus sed lobortis aliquam lorem blandit. Lorem eu nunc metus col. Commodo id in arcu ante lorem
                    ipsum sed accumsan erat praesent faucibus commodo ac mi lacus. Adipiscing mi ac commodo. Vis aliquet
                    tortor ultricies non ante erat nunc integer eu ante ornare amet commetus vestibulum blandit integer
                    in curae ac faucibus integer non. Adipiscing cubilia elementum.</p>
            """},
            {'num': 2, 'name': 'Things I Can Do', 'id': 'two', 'content': """
               <h3>Things I Can Do</h3>

                <p>Integer eu ante ornare amet commetus vestibulum blandit integer in curae ac faucibus integer non.
                    Adipiscing cubilia elementum integer lorem ipsum dolor sit amet.</p>
                <ul class="feature-icons">
                    <li class="fa-code">Write all the code</li>
                    <li class="fa-cubes">Stack small boxes</li>
                    <li class="fa-book">Read books and stuff</li>
                    <li class="fa-coffee">Drink much coffee</li>
                    <li class="fa-bolt">Lightning bolt</li>
                    <li class="fa-users">Shadow clone technique</li>
                </ul>
            """},
            {'num': 3, 'name': 'A Few Accomplishments', 'id': 'three', 'content': """
                 <h3>A Few Accomplishments</h3>

                <p>Integer eu ante ornare amet commetus vestibulum blandit integer in curae ac faucibus integer non.
                    Adipiscing cubilia elementum integer. Integer eu ante ornare amet commetus.</p>

                <div class="features">
                    <article>
                        <a href="#" class="image"><img src="./static/images/pic01.jpg" alt=""/></a>

                        <div class="inner">
                            <h4>Possibly broke spacetime</h4>

                            <p>Integer eu ante ornare amet commetus vestibulum blandit integer in curae ac faucibus
                                integer adipiscing ornare amet.</p>
                        </div>
                    </article>
                    <article>
                        <a href="#" class="image"><img src="./static/images/pic02.jpg" alt=""/></a>

                        <div class="inner">
                            <h4>Terraformed a small moon</h4>

                            <p>Integer eu ante ornare amet commetus vestibulum blandit integer in curae ac faucibus
                                integer adipiscing ornare amet.</p>
                        </div>
                    </article>
                    <article>
                        <a href="#" class="image"><img src="./static/images/pic03.jpg" alt=""/></a>

                        <div class="inner">
                            <h4>Snapped dark matter in the wild</h4>

                            <p>Integer eu ante ornare amet commetus vestibulum blandit integer in curae ac faucibus
                                integer adipiscing ornare amet.</p>
                        </div>
                    </article>
                </div>
            """},
            {'num': 4, 'name': 'Contact', 'id': 'four', 'content': """
   <h3>Contact Me</h3>

                <p>Integer eu ante ornare amet commetus vestibulum blandit integer in curae ac faucibus integer non.
                    Adipiscing cubilia elementum integer. Integer eu ante ornare amet commetus.</p>

                <form method="post" action="#">
                    <div class="row uniform">
                        <div class="6u 12u(3)"><input type="text" name="name" id="name" placeholder="Name"/></div>
                        <div class="6u 12u(3)"><input type="email" name="email" id="email" placeholder="Email"/></div>
                    </div>
                    <div class="row uniform">
                        <div class="12u"><input type="text" name="subject" id="subject" placeholder="Subject"/></div>
                    </div>
                    <div class="row uniform">
                        <div class="12u"><textarea name="message" id="message" placeholder="Message"
                                                   rows="6"></textarea></div>
                    </div>
                    <div class="row uniform">
                        <div class="12u">
                            <ul class="actions">
                                <li><input type="submit" class="special" value="Send Message"/></li>
                                <li><input type="reset" value="Reset Form"/></li>
                            </ul>
                        </div>
                    </div>
                </form>
            """},

        ]
        table.insert_many(sections, ordered=True)
        #########
        all_sections = list(table.find().sort('num', pymongo.ASCENDING))
        # sec_list = list()
        # for sec in all_sections:
        #     sec_list.append(sec)
        self.render('index.html', sections=all_sections)
