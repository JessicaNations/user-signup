from flask import Flask, request
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
	template = jinja_env.get_template('home_page.html')
	return template.render()

@app.route("/hello", methods=['POST'])
def hello():
	form_username = request.form['username']
	template = jinja_env.get_template('welcome_page.html')
	return template.render(username=form_username)


app.run()