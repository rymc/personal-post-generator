from bs4 import BeautifulSoup
from slugify import slugify
from jinja2 import Environment, FileSystemLoader
import os, re


root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment( loader = FileSystemLoader(templates_dir) )
template = env.get_template('post.html')

html =  open('index.html', 'r').read()
soup = BeautifulSoup(html, 'html5lib')

posts = soup.find_all(class_='pContainer')

for post in posts:
	title = post.find('h1').find('a', href=True).string
	filename = slugify(title)
	post.find('h1').find('a', href=True)['href'] = '/blog/post/'+filename
	post.find('h1').find('a', href=True)['target'] = '_blank'

	with open('post/'+filename, 'w') as fh:
		fh.write(template.render(
			post = post.prettify(formatter='html')
		))

newindex = soup.prettify(formatter='html')

with open('index.html', 'w') as w:
	w.write(newindex)
