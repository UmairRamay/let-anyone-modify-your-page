import os

import jinja2
import webapp2

#template_dir = os.path.join(os.path.dirname(_file_), 'templates')
#jinja_env = jinja2.Enviroment(loader = jinja2.FileSystemLoader(template_dir))


#Udacity Code is Now Working So Using This Instead
template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_environment = jinja2.Environment(autoescape=True, loader=jinja2.FileSystemLoader(template_dir))


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
	   self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_environment.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


#For Generating the Notes
class MainPage(Handler):
    def get(self):
        items = self.request.get_all("notes")
        self.render("user_add_notes.html", items = items)

class UserHandler(Handler):
    def get(self):
        n = self.request.get('n', 0)
        n =  n and int(n)
        self.render('user.html', n = n)
              
       
       
		

app = webapp2.WSGIApplication([('/', MainPage),
('/user', UserHandler),
], debug=True)
