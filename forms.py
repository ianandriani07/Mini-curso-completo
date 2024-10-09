from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class Materia(FlaskForm):
    id_materia = IntegerField("ID da Matéria", render_kw={"placeholder": "Digite seu id"}, validators=[DataRequired()])
    nome = StringField("Nome", render_kw={"placeholder": "Digite o nome da matéria"}, validators=[DataRequired()])
    professor = StringField("Professor", render_kw={"placeholder": "Digite nome do professor(a)"}, validators=[DataRequired()])
    enviar = SubmitField("Enviar")
