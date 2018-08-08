import webapp2
from random import shuffle
import jinja2
import os
from models import MadLib

#libraries for APIs
from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
def run_query(user_story,spaces):
    mad_lib = MadLib(story=user_story, num_spaces=spaces)
    key = mad_lib.put
    print("!!!!!!!!!!!!!!!!!!!!")
    print(key)



class HomePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/Home_Page.html')
        self.response.write(about_template.render())
   
class UniPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/Uni_page.html')
        self.response.write(about_template.render())
        
class TechPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/Tech_page.html')
        self.response.write(about_template.render())
        
class SportsPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/Sports_page.html')
        self.response.write(about_template.render())

class AniPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/Ani_page.html')
        self.response.write(about_template.render())
        
class BedPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/Bed_page.html')
        self.response.write(about_template.render())
        
class BePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/Be_page.html')
        self.response.write(about_template.render())
    
        
class ResultPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/Result_page.html')
        self.response.write(about_template.render())

         

    def post(self):
        flag = True
        if (flag):
            self.response.write(self.request.get('first_input'))
        else: 
            self.redirect("/")
            
class BeCreativeHandler(webapp2.RequestHandler):
    def post(self): 
       #TODO: to get user impot from becreatice.html
        run_query("this is a (adjecive) story",1)

   



app = webapp2.WSGIApplication([
    ('/',HomePage),
    ('/uni',UniPage),
    ('/tech', TechPage), 
    ('/sports', SportsPage), 
    ('/ani', AniPage), 
    ('/bed', BedPage), 
    ('/be', BePage), 
<<<<<<< HEAD
    ('/result', ResultPage)

    
    
=======
<<<<<<< HEAD
    ('/result', ResultPage)
=======
    ('/result', ResultPage), 
<<<<<<< HEAD
    ('/becreative',BeCreativeHandler),
=======
<<<<<<< HEAD
    
    
    
], debug=True)
=======
<<<<<<< HEAD

    
=======
>>>>>>> fcb3b85a774337ae68ac0b261c70de458756840c
>>>>>>> 040d7f192bb59aa5e98bf68ce216fbd13298b37d
>>>>>>> b50c8588e64301a2f5a0848df90a85c2156fef79
>>>>>>> efb73354ceac9aa5b1c008446bf7a5e4855d2448
    
], debug=True)
