# -*- coding: utf-8 -*-

from os.path import join, dirname, abspath
from flask import Flask, render_template, request, redirect
from time import sleep
import json


app = Flask(
    __name__,
    static_url_path = '',
    static_folder = 'public',
    template_folder = 'templates'
)

# App configuration
directory = dirname(abspath(__file__))
config_file = join(directory, 'portal.conf')
locale_file = join(join(directory, 'locale'), '%s.json')
config_file = join(directory, 'credentials.csv')
app.config.from_pyfile(config_file)


@app.route('/')
def root():
    return redirect('/portal')

@app.route('/login', methods = ['POST'])
def login():
    save_credentials(request.form)
    sleep(3) # Simulating some internet related delay
    return redirect('/error') # Oh no! >:)

@app.route('/<page>')
def send_page(page):
    try:
        page_content = app.config['LOCALE'][page]
    except:
        page = 'not_found'
        page_content = app.config['LOCALE'][page]
    back = page != 'portal'
    return render_template(
        '%s.html' % page,
        page = page_content,
        back = back
    )


def get_locale(lang = 'en'):
    filename = locale_file % lang
    with open(filename) as f:
        return json.load(f)

def save_credentials(form):
    type = form.get('type')
    username = form.get('username')
    email = form.get('email')
    username += ':' + email if email else ''
    password = form.get('password')
    repeat = form.get('repeat')
    f = open(credentials_file, 'a')
    f.write("%s,%s,%s,%s\n" % (
        type,
        username,
        password,
        repeat
    ))
    f.close()


if __name__ == '__main__':
    app.config['LOCALE'] = get_locale(app.config['LANG'])
    app.run(
        host = app.config['HOST'],
        port = app.config['PORT'],
        debug = app.config['DEBUG'],
        threaded = True
    )
