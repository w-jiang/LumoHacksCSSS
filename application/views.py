from application import application
from flask import Flask, Response, render_template, request, json, redirect, flash, url_for, Markup, make_response, stream_with_context

@application.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

@application.route('/')
@application.route('/index')
def index():
    return redirect(url_for('homePage'))

@application.route('/homePage')
def homePage():
    return render_template('index.html')

@application.route('/myJournals')
def myJournals():
    return render_template('myJournals.html')