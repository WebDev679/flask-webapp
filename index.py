from flask import Flask as flask
from flask import redirect, render_template, url_for, session, request, Blueprint

index_api = Blueprint('index_api', __name__)

@index_api.route('/home', methods = ["GET", "POST"])
def index():
    
