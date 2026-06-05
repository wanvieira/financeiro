from models import db

class Parcelamento(db.Model):

    __tablename__ = 'parcelamentos'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    loja = db.Column(
        db.String(200),
        nullable=False
    )

    valor_parcela = db.Column(
        db.Float,
        nullable=False
    )

    parcelas_restantes = db.Column(
        db.Integer,
        nullable=False
    )

    categoria = db.Column(
        db.String(100),
        nullable=True
    )