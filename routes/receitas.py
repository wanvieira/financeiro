from flask import Blueprint, render_template

receitas_bp = Blueprint(
    'receitas',
    __name__,
    url_prefix='/receitas'
)

@receitas_bp.route('/')
def index():

    return render_template('receitas.html')