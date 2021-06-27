#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# LICENSE:
# *********************************************************************
# *
# *********************************************************************
#

"""
"""

__version__ = "0.1"
__revisison__ = "0.1"
__author__ = "Shawn C.H. Chiou"
__authorcontact__ = "shawn.chiou@gmail.com"
__website__ = ""

import os, sys, re, codecs
import bottle
from beaker.middleware import SessionMiddleware
from docutils import core, io

@bottle.route('/')
def index():
    # Redirect to home page by default
    bottle.redirect('/home')

@bottle.route('/js/<filename>')
def load_js(filename):
    return bottle.static_file(filename, root='./js')

@bottle.route('/css/<filename>')
def load_css(filename):
    return bottle.static_file(filename, root='./css')

@bottle.route('/images/<filename>')
def load_image(filename):
    return bottle.static_file(filename, root='./images')

@bottle.route('/login')
def login():
    # Open session
    session = bottle.request.environ.get('beaker.session')

    data = {}

    if 'current_url' in session:
        data['back_url'] = session['current_url']
    else:
        data['back_url'] = '/'

    return bottle.template('login', data = data)

@bottle.route('/pref')
def pref():
    # ToDo!
    # load users' setting
    return bottle.template('pref', data = data)

@bottle.route('/<page_name>')
def load_page(page_name):
    # Open session
    session = bottle.request.environ.get('beaker.session')
    #if 'current_url' in session: print session['current_url']

    # Filter
    if page_name == 'favicon.ico' or page_name == 'FAVICON.ICO':
        bottle.redirect('/images/' + page_name)

    # Page not exist? create new page.
    if not os.path.exists(PAGE_PATH + page_name + PAGE_EXT):
        bottle.redirect('/acts/add/' + page_name)

    data = {}
    data['title'] = page_name

    # Get raw content and parse
    f = open(PAGE_PATH + page_name + PAGE_EXT, 'r')
    data['content'] = rst2html(f.read())
    f.close()

    # Save URL track
    session['current_url'] = bottle.request.fullpath
    session.save()

    # Render page
    return bottle.template('page', data = data)

@bottle.route('/acts/add/<page_name>')
def add(page_name):
    session = bottle.request.environ.get('beaker.session')

    data = {}
    data['action'] = 'Add'
    data['title'] = page_name
    data['content'] = ''

    # Check if the session key existed
    if 'current_url' in session:
        data['back_url'] = session['current_url']
    else:
        # Return to home if no current URL existed
        data['back_url'] = '/'

    return bottle.template('form', data = data)

@bottle.route('/acts/edit/<page_name>')
def edit(page_name):
    session = bottle.request.environ.get('beaker.session')

    data = {}
    data['action'] = 'Edit'
    data['title'] = page_name

    # Check if the session key existed
    if 'current_url' in session:
        data['back_url'] = session['current_url']
    else:
        # Return to home if no current URL existed
        data['back_url'] = '/'

    if os.path.exists(PAGE_PATH + page_name + PAGE_EXT):
        f = open(PAGE_PATH + page_name + PAGE_EXT, 'r')
        data['content'] = f.read()
        f.close()

    return bottle.template('form', data = data)

@bottle.route('/acts/save/<page_name>', method='POST')
def save(page_name):
    # Save all changes into file
    try:
	# For open file with specified encoding (UTF-8), use codecs instead
        #f = open(PAGE_PATH + page_name + PAGE_EXT, 'w')
        f = codecs.open(PAGE_PATH + page_name + PAGE_EXT, encoding='utf-8', mode='w+')
        f.write(bottle.request.forms.content)
    except IOError:
        print "Can not write " + page_name
    except:
        print "Unknown error: "
        print sys.exc_info()[0]
        raise
    finally:
        f.close()

    # Redirect to changed page
    bottle.redirect('/' + page_name)

@bottle.route('/acts/auth', method='POST')
def auth():
    session = bottle.request.environ.get('beaker.session')

    # Get parameters
    if bottle.request.forms.get('login') == '' or \
       bottle.request.forms.get('password') == '':
        print 'Failed!'
        return False
        #if 'current_url' in session:
        #    bottle.redirect(session['current_url'])
        #else:
        #    bottle.redirect('/')

    login = bottle.request.forms.get('login')
    password = bottle.request.forms.get('password')

    # Connect to DB
    print login
    print password

    # Session registering
    print 'Success!'
    return True

@bottle.route('/acts/logout')
def logout():
    session = bottle.request.environ.get('beaker.session')

    # Remove from session

    # Return to home page after logout
    bottle.redirect('/')

def rst2html(rst_string):
    overrides = {
        'input_encoding': 'utf8',
        'doctitle_xform': 1,
        'initial_header_level': 1
    }

    output = core.publish_parts(
        source = rst_string,
        source_path = None, destination_path = None,
        writer_name = 'html', settings_overrides = overrides
    )

    pattern_img = "<img.*?>"
    p = re.compile(pattern_img)
    matched_list = p.findall(output['html_body'])

    for matched in matched_list:
        p_src = re.compile('src=\".*?\"')
        splited = re.split('[\W]+', matched)
	print splited[7] + "." + splited[8]

    return output['html_body']

# Start execution
if __name__ == '__main__':
    bottle.debug(True)
    bottle.TEMPLATES.clear()

    DOC_ROOT = os.getcwd() + '/'

    PAGE_PATH = DOC_ROOT + 'pages/'
    UPLOAD_PATH = DOC_ROOT + 'uploads/'

    PAGE_EXT = '.rst'

    # Session setting
    session_opts = {
        'session.type': 'file',
        'session.cookie_expires': 300,
        'session.data_dir': '/tmp',
        'session.auto': True
    }

    # Session initial
    app = SessionMiddleware(bottle.app(), session_opts)

    bottle.run(app=app, host='0.0.0.0', port=8080, reloader=True)
