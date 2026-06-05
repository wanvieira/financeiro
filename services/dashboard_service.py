from models.parcelamento import Parcelamento
from models.despesa import Despesa
from models.receita import Receita


def resumo_financeiro():

    total_receitas = 0
    total_despesas = 0
    total_parcelamentos = 0

    # SOMA RECEITAS
    receitas = Receita.query.all()

    for receita in receitas:

        total_receitas += receita.valor

    # SOMA DESPESAS
    despesas = Despesa.query.all()

    for despesa in despesas:

        total_despesas += despesa.valor

    # SOMA PARCELAMENTOS
    parcelamentos = Parcelamento.query.all()

    for parcela in parcelamentos:

        total_parcelamentos += (
            parcela.valor_parcela *
            parcela.parcelas_restantes
        )

    saldo = (
        total_receitas -
        total_despesas -
        total_parcelamentos
    )

    return {

        'receitas': round(total_receitas, 2),

        'despesas': round(total_despesas, 2),

        'parcelamentos': round(total_parcelamentos, 2),

        'saldo': round(saldo, 2)

    }