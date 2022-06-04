from flask import Flask, jsonify

app = Flask(__name__)

contas = [
    {
        'id': 'imt',
        'senha': '123',
        'status': True,
        'clean': True,
        'delete': True
    },
    {
        'id': 'imt',
        'senha': '123',
        'status': True,
        'clean': True,
        'delete': True
    },
    {
        'id': 'imt2',
        'senha': '123',
        'status': True,
        'clean': True,
        'delete': True
    },
    {
        'id': 'imt3',
        'senha': '123',
        'status': True,
        'clean': True,
        'delete': True
    },
    {
        'id': 'Teste',
        'senha': 'qwe',
        'status': False,
        'clean': False,
        'delete': False
    }
]

@app.route('/')

def raiz():

    return ''

@app.route('/contas/<string:id>/<string:senha>')

def login(id, senha):

    for conta in contas:

        if id == conta['id']:

            if senha == conta['senha']:

                return jsonify({'status': conta['status']},
                               {'clean': conta['clean']},
                               {'delete': conta['delete']})

            else:

                return jsonify({'status': False})

    else:

        return jsonify({'status': ''})

if __name__ == "__main__":

    app.run(debug=True)


