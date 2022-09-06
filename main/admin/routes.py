from flask import Blueprint, session, redirect

admins = Blueprint('admins', __name__)


@admins.route('/home/')
def home():
    return '///////////////////////////////'


# /change-language/tk
@admins.route('/change-language/<code>')
def change_language(code):
    session['language'] = code
    return redirect('/azyk_haryt/')
    #return {'language': session['language']}
