from flask import Blueprint, render_template, request, redirect

from models import db
from models.parcelamento import Parcelamento

parcelamentos_bp = Blueprint(
    'parcelamentos',
    __name__,
    url_prefix='/parcelamentos'
)


# LISTAR PARCELAMENTOS
@parcelamentos_bp.route('/')
def listar():

    dados = Parcelamento.query.all()

    total_geral = sum(
        item.valor_parcela * item.parcelas_restantes
        for item in dados
    )

    total_mensal = sum(
        item.valor_parcela
        for item in dados
    )

    return render_template(
        'parcelamentos.html',
        dados=dados,
        total_geral=total_geral,
        total_mensal=total_mensal
    )


# NOVO PARCELAMENTO
@parcelamentos_bp.route('/novo', methods=['POST'])
def novo_parcelamento():

    novo = Parcelamento(
        loja=request.form['loja'],
        valor_parcela=float(request.form['valor_parcela']),
        parcelas_restantes=int(request.form['parcelas_restantes']),
        categoria=request.form['categoria']
    )

    db.session.add(novo)

    db.session.commit()

    return redirect('/parcelamentos/')


# EXCLUIR PARCELAMENTO
@parcelamentos_bp.route('/excluir/<int:id>', methods=['POST'])
def excluir_parcelamento(id):

    parcelamento = Parcelamento.query.get(id)

    if parcelamento:

        db.session.delete(parcelamento)

        db.session.commit()

    return redirect('/parcelamentos/')