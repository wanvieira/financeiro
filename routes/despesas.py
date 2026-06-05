from flask import Blueprint, render_template

despesas_bp = Blueprint(
    'despesas',
    __name__,
    url_prefix='/despesas'
)

@despesas_bp.route('/')
def index():

    return render_template('despesas.html')