from flask import *
from datetime import datetime
from sqlalchemy import create_engine, Column, Date, Integer, String, Text, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///database.db'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()


class Consulta(Base):
    __tablename__ = 'consulta'

    id = Column(Integer, primary_key=True)
    paciente = Column(String(80), nullable=False)
    data_consulta = Column(Date, nullable=False)
    hora_consulta = Column(Time, nullable=False)
    informacoes_adicionais = Column(Text)

    def __repr__(self):
        return f"Consulta({self.cliente_nome}, {self.data_consulta}, {self.hora_consulta})"


Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def home():
    consultas = db.query(Consulta).all()
    return render_template('home.html', consultas=consultas)

@app.route('/deletar_consulta/<int:consulta_id>', methods=['GET'])
def deletar_consulta(consulta_id):
    consulta = db.query(Consulta).get(consulta_id)
    if consulta:
        db.delete(consulta)
        db.commit()
    return redirect('/')


@app.route('/editar', methods=['POST'])
def editar_consulta():
    consulta = db.query(Consulta).get(request.form['id'])
    consulta.paciente = request.form['paciente']
    consulta.data_consulta = datetime.strptime(request.form['data_consulta'], '%Y-%m-%d').date()
    consulta.hora_consulta = datetime.strptime(request.form['hora_consulta'], '%H:%M').time()
    consulta.informacoes_adicionais = request.form.get('informacoes_adicionais', None)

    db.commit()
    return redirect('/')

@app.route('/cadastro', methods=['POST'])
def cadastro():
    paciente = request.form['paciente']
    data_consulta = datetime.strptime(
        request.form['data_consulta'], '%Y-%m-%d').date()
    hora_consulta = datetime.strptime(
        request.form['hora_consulta'], '%H:%M').time()
    informacoes_adicionais = request.form.get('informacoes_adicionais', None)

    nova_consulta = Consulta(paciente=paciente, data_consulta=data_consulta,
                             hora_consulta=hora_consulta, informacoes_adicionais=informacoes_adicionais)

    db.add(nova_consulta)
    db.commit()

    return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and request.form['username'] == 'admin' and request.form['senha'] == 'admin':
        session['logado'] = True
        return redirect('/')
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
