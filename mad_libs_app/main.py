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
        noun1 = self.request.get("noun1")
        noun2 = self.request.get("noun2")
        noun3 = self.request.get("noun3")
        noun4 = self.request.get("noun4")
        noun5 = self.request.get("noun5")
        noun6 = self.request.get("noun6")
        noun7 = self.request.get("noun7")
        noun8 = self.request.get("noun8")
        noun9 = self.request.get("noun9")
        verb1 = self.request.get("verb1")
        verb2 = self.request.get("verb2")
        verb3 = self.request.get("verb3")
        adjective1 = self.request.get("adjective1")
        adjective2 = self.request.get("adjective2")
        adjective3 = self.request.get("adjective3")
        adverb1 = self.request.get("adverb1")
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
            "verb1_key": verb1,
            "verb2_key": verb2,
            "verb3_key": verb3,
            "adj1_key": adjective1,
            "adj2_key": adjective2,
            "adj3_key": adjective3,
            "adv1_key": adverb1,
            "category_key": "uni"
            
        } 
        
        self.response.write(about_template.render(the_variable_dict))
    def get(self):
        
        mad_lib_inputs =[
            {
                "part_of_speech": "noun1",
            },
            {
                 "part_of_speech": "adverb1",
            },
            {
                 "part_of_speech": "verb1",
            },
            {
                 "part_of_speech": "noun2",
            },
            {
                 "part_of_speech": "adjective1",
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
                 "part_of_speech": "noun7",
            },
            {
                 "part_of_speech": "noun8",
            },
            {
                 "part_of_speech": "noun9",
            },
            {
                 "part_of_speech": "verb2",
            },
            {
                 "part_of_speech": "adjective2",
            },
            {
                 "part_of_speech": "adjective3",
            },
            {
                 "part_of_speech": "verb3",
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
        verb1 = self.request.get("verb1")
        verb2 = self.request.get("verb2")
        adjective1 = self.request.get("adjective1")
        adjective2 = self.request.get("adjective2")
        adjective3 = self.request.get("adjective3")
        number1 = self.request.get("number1")
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
            "verb1_key": verb1,
            "verb2_key": verb2,
            "adj1_key": adjective1,
            "adj2_key": adjective2,
            "adj3_key": adjective3,
            "num_key": number1,
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
        verb1 = self.request.get("verb1")
        verb2 = self.request.get("verb2")
        verb3 = self.request.get("verb3")
        verb4 = self.request.get("verb4")
        adjective1 = self.request.get("adjective1")
        adjective2 = self.request.get("adjective2")
        adjective3 = self.request.get("adjective3")
        number1 = self.request.get("number1")
        number2 = self.request.get("number2")
        number3 = self.request.get("number3")
        number4 = self.request.get("number4")
        adverb1 = self.request.get("adverb1")
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
            "verb1_key": verb1,
            "verb2_key": verb2,
            "verb3_key": verb3,
            "verb4_key": verb4,
            "adj1_key": adjective1,
            "adj2_key": adjective2,
            "adj3_key": adjective3,
            "num1_key": number1,
            "num2_key": number2,
            "num3_key": number3,
            "num4_key": number4,
            "adv1_key":adverb1,
            "category_key": "sports"
            
        } 
        
        self.response.write(about_template.render(the_variable_dict))
    def get(self):
        
        mad_lib_inputs =[
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
                 "part_of_speech": "number1",
            },
            {
                 "part_of_speech": "adjective1",
            },
            {
                 "part_of_speech": "adjective2",
            },
            {
                 "part_of_speech": "verb1",
            },
            {
                 "part_of_speech": "verb2",
            },
            {
                 "part_of_speech": "noun4",
            },
            {
                 "part_of_speech": "number2",
            },
            {
                 "part_of_speech": "adverb1",
            },
            {
                 "part_of_speech": "noun5",
            },
            {
                 "part_of_speech": "verb3",
            },
            {
                 "part_of_speech": "number3",
            },
            {
                 "part_of_speech": "number4",
            },
            {
                 "part_of_speech": "noun6",
            },
            {
                 "part_of_speech": "verb4",
            },
            {
                 "part_of_speech": "noun7",
            },
            {
                 "part_of_speech": "adjective3",
            },
            {
                 "part_of_speech": "noun8",
            },
            {
                 "part_of_speech": "noun9",
            },
            {
                 "part_of_speech": "noun10",
            },
            {
                 "part_of_speech": "noun11",
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
        noun1 = self.request.get("noun1")
        noun2 = self.request.get("noun2")
        noun3 = self.request.get("noun3")
        noun4 = self.request.get("noun4")
        noun5 = self.request.get("noun5")
        noun6 = self.request.get("noun6")
        noun7 = self.request.get("noun7")
        noun8 = self.request.get("noun8")
        noun9 = self.request.get("noun9")
        verb1 = self.request.get("verb1")
        verb2 = self.request.get("verb2")
        verb3 = self.request.get("verb3")
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
            "verb1_key": verb1,
            "verb2_key": verb2,
            "verb3_key": verb3,
            "category_key": "ani"
            
        } 
        
        self.response.write(about_template.render(the_variable_dict))
    def get(self):
        
        mad_lib_inputs =[
            {
                 "part_of_speech": "noun1",
            },
            {
                 "part_of_speech": "noun2",
            },
            {
                 "part_of_speech": "verb1",
            },
            {
                 "part_of_speech": "noun3",
            },
            {
                 "part_of_speech": "noun4",
            },
            {
                 "part_of_speech": "verb2",
            },
            {
                 "part_of_speech": "number1",
            },
            {
                 "part_of_speech": "verb3",
            },
            {
                 "part_of_speech": "noun5",
            },
            {
                 "part_of_speech": "noun6",
            },
            {
                 "part_of_speech": "noun7",
            },
            {
                 "part_of_speech": "noun8",
            },
            {
                 "part_of_speech": "noun9",
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
        verb1 = self.request.get("verb1")
        verb2 = self.request.get("verb2")
        adjective1 = self.request.get("adjective1")
        adjective2 = self.request.get("adjective2")
        adjective3 = self.request.get("adjective3")
        adjective4 = self.request.get("adjective4")
        adjective5 = self.request.get("adjective5")
        number1 = self.request.get("number1")
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
            "verb1_key": verb1,
            "verb2_key": verb2,
            "adj1_key": adjective1,
            "adj2_key": adjective2,
            "adj3_key": adjective3,
            "adj4_key": adjective4,
            "adj5_key": adjective5,
            "num1_key": number1,
            "category_key": "bed"
            
        } 
        
        self.response.write(about_template.render(the_variable_dict))
    def get(self):
        
        mad_lib_inputs =[
            {
                "part_of_speech": "noun1",
            },
            {
                 "part_of_speech": "adjective1",
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
                 "part_of_speech": "adjective2",
            },
            {
                 "part_of_speech": "noun6",
            },
            {
                 "part_of_speech": "adjective3",
            },
            {
                 "part_of_speech": "noun7",
            },
            {
                 "part_of_speech": "noun8",
            },
            {
                 "part_of_speech": "noun9",
            },
            {
                 "part_of_speech": "noun10",
            },
            {
                 "part_of_speech": "noun11",
            },
            {
                 "part_of_speech": "verb1",
            },
            {
                 "part_of_speech": "number1",
            },
            {
                 "part_of_speech": "noun12",
            },
            {
                 "part_of_speech": "adjective4",
            },
            {
                 "part_of_speech": "adjective5",
            },
            {
                 "part_of_speech": "verb2",
            }
        ]    

        the_variable_dict = {
            
            "chosen_madlib": mad_lib_inputs
            
        }
        
        about_template = the_jinja_env.get_template('templates/Bed_page.html')
        self.response.write(about_template.render(the_variable_dict))
        
class BestPage(webapp2.RequestHandler):
    def post(self):
        about_template = the_jinja_env.get_template('templates/Result_page.html')
        noun1 = self.request.get("noun1")
        noun2 = self.request.get("noun2")
        noun3 = self.request.get("noun3")
        noun4 = self.request.get("noun4")
        verb1 = self.request.get("verb1")
        verb2 = self.request.get("verb2")
        adjective1 = self.request.get("adjective1")
        adjective2 = self.request.get("adjective2")
        adjective3 = self.request.get("adjective3")
        adjective4 = self.request.get("adjective4")
        adjective5 = self.request.get("adjective5")
        the_variable_dict = {
            
            "noun1_key": noun1, 
            "noun2_key": noun2, 
            "noun3_key": noun3, 
            "noun4_key": noun4, 
            "verb1_key": verb1,
            "verb2_key": verb2,
            "adj1_key": adjective1,
            "adj2_key": adjective2,
            "adj3_key": adjective3,
            "adj4_key": adjective4,
            "adj5_key": adjective5,
            "category_key": "best"
            
        } 
        
        self.response.write(about_template.render(the_variable_dict))
    def get(self):
        mad_lib_inputs =[
            {
                 "part_of_speech": "noun1",
            },
            {
                 "part_of_speech": "noun2",
            },
            {
                 "part_of_speech": "verb1",
            },
            {
                 "part_of_speech": "adjective1",
            },
            {
                 "part_of_speech": "adjective2",
            },
            {
                 "part_of_speech": "adjective3",
            },
            {
                 "part_of_speech": "adjective4",
            },
            {
                 "part_of_speech": "adjective5",
            },
            {
                 "part_of_speech": "noun3",
            },
            {
                 "part_of_speech": "verb2",
            },
            {
                 "part_of_speech": "noun4",
            }
            
        ]    

        the_variable_dict = {
            
            "chosen_madlib": mad_lib_inputs
            
        }
        
        about_template = the_jinja_env.get_template('templates/Best_page.html')
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
    ('/best', BestPage), 
    ('/result', ResultPage), 
], debug=True)