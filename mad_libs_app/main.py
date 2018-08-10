import webapp2
from random import shuffle
import jinja2
import os
#from models import MadLib

#libraries for APIs
from google.appengine.api import urlfetch
import json


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


#def run_query(user_story,spaces):
    #mad_lib = MadLib(story=user_story, num_spaces=spaces)
    
    #key = mad_lib.put
    #print("!!!!!!!!!!!!!!!!!!!!")
    #print(key)



class HomePage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/Home_Page.html')
        self.response.write(about_template.render())
   
class UniPage(webapp2.RequestHandler):
    def post(self):
        about_template = the_jinja_env.get_template('templates/Result_page.html')
        noun = self.request.get("noun")
        verb = self.request.get("verb")
        adjective = self.request.get("adj")
        number = self.request.get("num")
        adverb = self.request.get("adv")
        the_variable_dict = {
            
            "noun_key": noun, 
            "verb_key": verb,
            "adj_key": adjective,
            "num_key": number,
            "adv_key":adverb,
            "category_key": "uni"
            
        } 
        
        self.response.write(about_template.render(the_variable_dict))
    def get(self):
        
        mad_lib_inputs =[
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "adverb",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "verb",
            }
            
        ]    

        the_variable_dict = {
            
            "chosen_madlib": mad_lib_inputs
            
        }
        
        about_template = the_jinja_env.get_template('templates/Uni_page.html')
        self.response.write(about_template.render(the_variable_dict))
        
        
class TechPage(webapp2.RequestHandler):
    def post(self):
        about_template = the_jinja_env.get_template('templates/Result_page.html')
        noun1 = self.request.get("noun1")
        noun2 = self.request.get("noun2")
        noun3 = self.request.get("noun3")
        noun4 = self.request.get("noun4")
        noun5 = self.request.get("noun5")
        noun6 = self.request.get("noun6")
        noun7 = self.request.get("noun7")
        noun8 = self.request.get("noun8")
        noun9 = self.request.get("noun9")
        noun10 = self.request.get("noun10")
        noun11= self.request.get("noun11")
        noun12= self.request.get("noun12")
        noun13= self.request.get("noun13")
        noun14= self.request.get("noun14")
        verb = self.request.get("verb")
        adjective = self.request.get("adj")
        number = self.request.get("num")
        adverb = self.request.get("adv")
        the_variable_dict = {
            
            "noun1_key": noun1, 
            "noun2_key": noun2, 
            "noun3_key": noun3, 
            "noun4_key": noun4, 
            "noun5_key": noun5, 
            "noun6_key": noun6, 
            "noun7_key": noun7, 
            "noun8_key": noun8, 
            "noun9_key": noun9, 
            "noun10_key": noun10, 
            "noun11_key": noun11, 
            "noun12_key": noun12, 
            "noun13_key": noun13, 
            "noun14_key": noun4, 
            "verb_key": verb,
            "adj_key": adjective,
            "num_key": number,
            "adv_key":adverb,
            "category_key": "tech"
            
        } 
        
        self.response.write(about_template.render(the_variable_dict))
    def get(self):
        
        mad_lib_inputs =[
            {
                "part_of_speech": "adjective1",
            },
            {
                 "part_of_speech": "noun1",
            },
            {
                 "part_of_speech": "noun2",
            },
            {
                 "part_of_speech": "noun3",
            },
            {
                 "part_of_speech": "noun4",
            },
            {
                 "part_of_speech": "noun5",
            },
            {
                 "part_of_speech": "noun6",
            },
            {
                 "part_of_speech": "adjective2",
            },
            {
                 "part_of_speech": "noun7",
            },
            {
                 "part_of_speech": "adjective3",
            },
            {
                 "part_of_speech": "verb1",
            },
            {
                 "part_of_speech": "noun8",
            },
            {
                 "part_of_speech": "verb2",
            },
            {
                 "part_of_speech": "noun9",
            },
            {
                 "part_of_speech": "noun10",
            },
            {
                 "part_of_speech": "number1",
            },
            {
                 "part_of_speech": "noun11",
            },
            {
                 "part_of_speech": "noun12",
            },
            {
                 "part_of_speech": "noun13",
            },
            {
                 "part_of_speech": "noun14",
            }
        ]    

        the_variable_dict = {
            
            "chosen_madlib": mad_lib_inputs
            
        }
        
        about_template = the_jinja_env.get_template('templates/Tech_page.html')
        self.response.write(about_template.render(the_variable_dict))
        
        
class SportsPage(webapp2.RequestHandler):
    def post(self):
        about_template = the_jinja_env.get_template('templates/Result_page.html')
        noun = self.request.get("noun")
        verb = self.request.get("verb")
        adjective = self.request.get("adj")
        number = self.request.get("num")
        adverb = self.request.get("adv")
        the_variable_dict = {
            
            "noun_key": noun, 
            "verb_key": verb,
            "adj_key": adjective,
            "num_key": number,
            "adv_key":adverb,
            "category_key": "sports"
            
        } 
        
        self.response.write(about_template.render(the_variable_dict))
    def get(self):
        
        mad_lib_inputs =[
            {
                "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "number",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "number",
            },
            {
                 "part_of_speech": "adverb",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "number",
            },
            {
                 "part_of_speech": "number",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            }
        ]    

        the_variable_dict = {
            
            "chosen_madlib": mad_lib_inputs
            
            
        }
        
        about_template = the_jinja_env.get_template('templates/Sports_page.html')
        self.response.write(about_template.render(the_variable_dict))
        

class AniPage(webapp2.RequestHandler):
    def post(self):
        about_template = the_jinja_env.get_template('templates/Result_page.html')
        noun = self.request.get("noun")
        verb = self.request.get("verb")
        adjective = self.request.get("adj")
        color = self.request.get("col")
        number = self.request.get("num")
        adverb = self.request.get("adv")
        the_variable_dict = {
              
            "noun_key": noun, 
            "verb_key": verb,
            "adj_key": adjective,
            "num_key": number,
            "adv_key":adverb,
            "category_key": "ani"
            
            
            

        } 
        
        self.response.write(about_template.render(the_variable_dict))
    def get(self):
        
        mad_lib_inputs =[
           {
                "part_of_speech": "number",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "color",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "number",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            }
        ]    

        the_variable_dict = {
            
            "chosen_madlib": mad_lib_inputs
            
        }
        
        about_template = the_jinja_env.get_template('templates/Ani_page.html')
        self.response.write(about_template.render(the_variable_dict))
        
class BedPage(webapp2.RequestHandler):
    def post(self):
        about_template = the_jinja_env.get_template('templates/Result_page.html')
        noun = self.request.get("noun")
        verb = self.request.get("verb")
        adjective = self.request.get("adj")
        number = self.request.get("num")
        adverb = self.request.get("adv")
        
        the_variable_dict = {
            
            "noun_key": noun, 
            "verb_key": verb,
            "adj_key": adjective,
            "num_key": number,
            "category_key": "bed"
            
        } 
        
        self.response.write(about_template.render(the_variable_dict))
    def get(self):
        
        mad_lib_inputs =[
            {
                "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "number",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "verb",
            }
        ]    

        the_variable_dict = {
            
            "chosen_madlib": mad_lib_inputs
            
        }
        
        about_template = the_jinja_env.get_template('templates/Bed_page.html')
        self.response.write(about_template.render(the_variable_dict))
        
class BePage(webapp2.RequestHandler):
    def post(self):
        about_template = the_jinja_env.get_template('templates/Result_page.html')
        noun = self.request.get("noun")
        verb = self.request.get("verb")
        adjective = self.request.get("adj")
        number = self.request.get("num")
        adverb = self.request.get("adv")
        the_variable_dict = {
            
            "noun_key": noun, 
            "verb_key": verb,
            "adj_key": adjective,
            "num_key": number,
            "category_key": "be"
            
        } 
        
        self.response.write(about_template.render(the_variable_dict))
    def get(self):
        
        mad_lib_inputs =[
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "adjective",
            },
            {
                 "part_of_speech": "noun",
            },
            {
                 "part_of_speech": "verb",
            },
            {
                 "part_of_speech": "noun",
            }
            
        ]    

        the_variable_dict = {
            
            "chosen_madlib": mad_lib_inputs
            
        }
        
        about_template = the_jinja_env.get_template('templates/Be_page.html')
        self.response.write(about_template.render(the_variable_dict))
        
    
        
class ResultPage(webapp2.RequestHandler):
    def get(self):
        about_template = the_jinja_env.get_template('templates/Result_page.html')
       
        self.response.write(about_template.render())
        
        



app = webapp2.WSGIApplication([
    ('/',HomePage),
    ('/uni',UniPage),
    ('/tech', TechPage), 
    ('/sports', SportsPage), 
    ('/ani', AniPage), 
    ('/bed', BedPage), 
    ('/be', BePage), 
    ('/result', ResultPage), 
], debug=True)
