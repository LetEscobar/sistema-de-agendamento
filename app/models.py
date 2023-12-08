from datetime import datetime
from app import db


class Consulta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_nome = db.Column(db.String(100), nullable=False)
    data_consulta = db.Column(db.Date, nullable=False)
    hora_consulta = db.Column(db.Time, nullable=False)
    informacoes_adicionais = db.Column(db.Text)

    def __repr__(self):
        return f"Consulta({self.cliente_nome}, {self.data_consulta}, {self.hora_consulta})"
