from application import application
from flask import Flask, Response, render_template, request, json, redirect, flash, url_for, Markup, make_response, stream_with_context

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')
    