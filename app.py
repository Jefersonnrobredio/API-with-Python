from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O Apanhador no Campo de Centeio',
        'autor': 'J.D. Salinger'
    },
    {
        'id': 2,
        'titulo': 'O Grande Gatsby',
        'autor': ' F. Scott Fitzgerald'
    },
    {
        'id': 3,
        'titulo': 'O Senhor dos Anéis',
        'autor': 'J.R.R. Tolkien'
    },
    {
        'id': 4,
        'titulo': 'Crônicas de Narnia',
        'autor': 'C.S. Lewis'
    },
    {
        'id': 5,
        'titulo': 'Dom Quixote',
        'autor': 'Miguel de Cervantes'
    },
    {
        'id': 6,
        'titulo': '"Cem Anos de Solidão',
        'autor': 'Gabriel Garcia Marquez'
    },
]


# consultar (todos)
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)


# consultar (id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


# editar(id)
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livre in enumerate(livros):
        if livros.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


# Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)


# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)


app.run(port=5000, host='localhost', debug=True)
