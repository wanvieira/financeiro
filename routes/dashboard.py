from flask import Blueprint, render_template, session, redirect

from services.dashboard_service import resumo_financeiro

dashboard_bp = Blueprint(
    'dashboard',
    __name__
)

@dashboard_bp.route('/inicio', strict_slashes=False)
def inicio():

    if not session.get('logado'):
        return redirect('/')

    return render_template('inicio.html')


@dashboard_bp.route('/dashboard', strict_slashes=False)
def dashboard():

    if not session.get('logado'):
        return redirect('/')

    resumo = resumo_financeiro()

    return render_template(
        'dashboard.html',
        resumo=resumo
    )