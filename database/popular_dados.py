import sys
import os

# =========================
# ADICIONA RAIZ DO PROJETO
# =========================

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

# =========================
# IMPORTS
# =========================

from app import app

from models import db

from models.despesa import Despesa
from models.parcelamento import Parcelamento
from models.receita import Receita

# =========================
# CONTEXTO FLASK
# =========================

with app.app_context():

    # =========================
    # LIMPA DADOS ANTIGOS
    # =========================

    Despesa.query.delete()
    Parcelamento.query.delete()
    Receita.query.delete()

    db.session.commit()

    # =========================
    # RECEITAS
    # =========================

    receitas = [

        Receita(
            descricao='Salário',
            valor=15000,
            categoria='Renda'
        )

    ]

    db.session.add_all(receitas)

    # =========================
    # DESPESAS À VISTA
    # =========================

    despesas = [

        Despesa(
            descricao='NETFLIX',
            valor=44.90,
            categoria='Streaming'
        ),

        Despesa(
            descricao='BURGER KING',
            valor=46.90,
            categoria='Alimentação'
        ),

        Despesa(
            descricao='SPOTIFY',
            valor=31.90,
            categoria='Streaming'
        ),

        Despesa(
            descricao='IFOOD CLUB',
            valor=5.95,
            categoria='Alimentação'
        ),

        Despesa(
            descricao='MC DONALDS',
            valor=65.90,
            categoria='Alimentação'
        ),

        Despesa(
            descricao='ALLIANZ SEGURO',
            valor=72.48,
            categoria='Seguro'
        ),

        Despesa(
            descricao='ASAAS FISIOSAUDE',
            valor=420.00,
            categoria='Saúde'
        ),

        Despesa(
            descricao='BELLAVIA',
            valor=214.59,
            categoria='Alimentação'
        ),

        Despesa(
            descricao='SANTINI ESMALTERIA',
            valor=185.00,
            categoria='Beleza'
        ),

        Despesa(
            descricao='PANIFICADORA SABOR',
            valor=46.25,
            categoria='Alimentação'
        ),

        Despesa(
            descricao='UNIVERSIDADE ESTÁCIO',
            valor=253.21,
            categoria='Educação'
        ),

        Despesa(
            descricao='UBER RIDES',
            valor=51.95,
            categoria='Transporte'
        ),

        Despesa(
            descricao='UBER TRIP',
            valor=122.98,
            categoria='Transporte'
        ),

        Despesa(
            descricao='POSTO SOBRADINHO',
            valor=140.00,
            categoria='Combustível'
        ),

        Despesa(
            descricao='COURSERA',
            valor=143.14,
            categoria='Educação'
        )

    ]

    db.session.add_all(despesas)

    # =========================
    # PARCELAMENTOS
    # =========================

    parcelamentos = [

        Parcelamento(
            loja='MSC CRUZEIROS',
            valor_parcela=890.87,
            parcelas_restantes=11,
            categoria='Lazer'
        ),

        Parcelamento(
            loja='DISTMACHADO',
            valor_parcela=333.33,
            parcelas_restantes=3,
            categoria='Casa'
        ),

        Parcelamento(
            loja='ADIDAS',
            valor_parcela=93.04,
            parcelas_restantes=9,
            categoria='Vestuário'
        ),

        Parcelamento(
            loja='LOJAS RENNER',
            valor_parcela=146.60,
            parcelas_restantes=1,
            categoria='Vestuário'
        ),

        Parcelamento(
            loja='SANTA LOLLA',
            valor_parcela=66.64,
            parcelas_restantes=1,
            categoria='Vestuário'
        ),

        Parcelamento(
            loja='IMPORTSG10',
            valor_parcela=347.22,
            parcelas_restantes=12,
            categoria='Tecnologia'
        ),

        Parcelamento(
            loja='GREEN TECNOLOGIA',
            valor_parcela=207.75,
            parcelas_restantes=9,
            categoria='Tecnologia'
        ),

        Parcelamento(
            loja='REFINANCIAMENTO FATURA',
            valor_parcela=2082.79,
            parcelas_restantes=6,
            categoria='Financeiro'
        ),

        Parcelamento(
            loja='TIM',
            valor_parcela=199.91,
            parcelas_restantes=4,
            categoria='Telefonia'
        )

    ]

    db.session.add_all(parcelamentos)

    # =========================
    # SALVA NO BANCO
    # =========================

    db.session.commit()

    print('DADOS INSERIDOS COM SUCESSO!')