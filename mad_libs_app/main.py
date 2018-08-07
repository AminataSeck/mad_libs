import webapp2
from random import shuffle
import jinja2
import os


#libraries for APIs
from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
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
   



app = webapp2.WSGIApplication([
    ('/',HomePage),
    ('/uni',UniPage),
    ('/tech', TechPage), 
    ('/sports', SportsPage), 
    ('/ani', AniPage), 
    ('/bed', BedPage), 
    ('/be', BePage), 
    ('/result', ResultPage)
    
], debug=True)

