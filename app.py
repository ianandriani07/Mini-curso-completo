from flask import Flask, jsonify, request, redirect, render_template
from forms import Materia

app = Flask(__name__)

app.config['SECRET_KEY'] = 'minha_chave_secreta'

materias = [
    {
        "id": 1,
        "nome": "Introdução a Engenharia de Computação",
        "professor(a)": "Eliane Pozzebom"
    },
    {
        "id": 2,
        "nome": "Linguagem de Programação 1",
        "professor(a)": "Anderson"
    }
]

@app.route('/materias', methods=['GET'])
def listar_materias():
    return jsonify(materias)

@app.route('/materia/<int:id_materia>', methods=['GET'])
def listar_materia(id_materia):
    
    for materia in materias:
        if materia['id'] == id_materia:
            return materia
    return "Matéria não encontrada"
        
@app.route('/remover-materia/<int:id_materia>', methods=['GET', 'DELETE'])
def remover_materia(id_materia):

    for materia in materias:
        if materia['id'] == id_materia:
            materias.remove(materia)
            return "Matéria removida com sucesso!"
    return "Matéria não encontrada"

@app.route('/adicionar-materia', methods=['POST'])
def adicionar_materia():

    id_materia = request.form['id_materia']
    nome = request.form['nome']
    professor = request.form['professor']

    materia = {"id": id_materia, "nome": nome, "professor(a)": professor}
    materias.append(materia)

    return "Materia adicionada com sucesso!"

@app.route('/atualizar-materia', methods=['POST'])
def atualizar_materia():
    id_materia = request.form['id_materia']
    nome = request.form['nome']
    professor = request.form['professor']

    for materia in materias:
        if materia['id'] == int(id_materia):
            materia['nome'] = nome
            materia['professor(a)'] = professor
            return "Matéria atualizada com sucesso!"
    return "Matéria não encontrada"
        
@app.route('/adicionar-materia', methods=['GET', 'POST'])
def adicionar_materia_template():
    form = Materia()
    return render_template('post.html', form=form)

@app.route('/atualizando-materia', methods=['GET', 'POST'])
def atualizar_materia_template():
    form = Materia()
    return render_template('put.html', form=form)

if __name__ == "__main__":
    app.run(port=8000)