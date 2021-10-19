from flask import Flask, app, request
from flask.json import jsonify
import json

app = Flask(__name__)

Receitas = [
    {
        "Título": "Mousse de morango",
        "Ingredientes": [
            "1 tang de morango"
            "1 caixa e meia de creme de leite"
            "1 leite condensado"
        ],
        "modo de preparo": "basta acrescentar tudo num liquidificador e misturar após misturado colocar em um recipiente e levar ao congelador por 4 horas.",
        "Redimento": "Rende 6 porções."
    },
]


@app.route("/rotaApiRest", methods=["POST", "GET"])
def Cadastro():
    if request.method == "GET":
        return jsonify(Receitas)
    elif request.method == "POST":
        newcadastro = json.loads(request.data)
        Receitas.append(newcadastro)
        return jsonify({
            "menssagem": "Cadastrado",
            "newValue": newcadastro

        })


@app.route('/rotaApiRest/<int:indice>', methods=['GET', 'PUT', 'DELETE'])
def cadastroID(indice):
    try:
        Receitas[indice]
    except IndexError:
        message = 'Receita ID {} Não Encontrada'.format(indice)
        return jsonify({
            "message": message,
            "status": "Error!"
        })
    except:
        message = 'Aconteceu um erro inesperado'
        return jsonify({
            "message": message,
            "status": "Error!"
        })

    if request.method == 'GET':
        return Receitas[indice]

    elif request.method == 'PUT':

        newValue = json.loads(request.data)

        Receitas[indice] = newValue
        return jsonify({
            "message": "Updated!",
            "newValue": newValue
        })
    elif request.method == 'DELETE':
        print(indice)
        Receitas.pop(indice)
        return jsonify({
            "message": "Deleted!",
            "arrayAtual": Receitas
        })


if __name__ == '_main_':
    app.run(debug=True)




