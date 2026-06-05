from models import db

class Despesa(db.Model):

    __tablename__ = 'despesas'

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    descricao = db.Column(
        db.String(200),
        nullable=False
    )

    valor = db.Column(
        db.Float,
        nullable=False
    )

    categoria = db.Column(
        db.String(100),
        nullable=True
    )