from flask import Flask, jsonify

app = Flask(__name__)

contas = [
    {
        'id': 'imt',
        'senha': '123',
        'status': True
    },
    {
        'id': 'imt2',
        'senha': '123',
        'status': True
    },
    {
        'id': 'imt3',
        'senha': '123',
        'status': False
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

                return jsonify({'status': conta['status']})

            else:

                return jsonify({'status': False})

    else:

        return ''

if __name__ == "__main__":

    app.run(debug=True)


