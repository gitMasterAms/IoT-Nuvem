from app import app
from flask import render_template, redirect, request, session, flash
from flask import send_file, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, SubmitField
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')