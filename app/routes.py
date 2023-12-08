from flask import Blueprint, render_template
from app.models import Consulta

main = Blueprint('main', __name__)


@main.route('/')
def home():
    consultas = Consulta.query.all()
    return render_template('home.html', consultas=consultas)
