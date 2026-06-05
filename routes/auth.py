from flask import Blueprint, render_template, request, redirect, session

auth_bp = Blueprint('auth', __name__)

SENHA_ADMIN = "oimeu123"

@auth_bp.route('/', methods=['GET', 'POST'])
def login():

    erro = None

    if request.method == 'POST':

        senha = request.form['senha']

        if senha == SENHA_ADMIN:

            session['logado'] = True

            return redirect('/inicio')

        else:
            erro = "Senha inválida"

    return render_template('login.html', erro=erro)