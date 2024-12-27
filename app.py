from flask import Flask, jsonify, request
from data_base_pokemon import data_base_pokemon

app = Flask(__name__)


@app.route('/pokemon', methods=['GET'])
def get_pokemon():
    # Obtém os query parameters
    pokemon_id = request.args.get('id')
    pokemon_name = request.args.get('name')
    pokemon_speciality = request.args.get('speciality')

    # Busca por ID
    if pokemon_id:
        for pokemon in data_base_pokemon:
            if pokemon['id'] == int(pokemon_id):
                return jsonify(pokemon)

    # Busca por Nome
    if pokemon_name:
        for pokemon in data_base_pokemon:
            if pokemon['name'].lower() == pokemon_name.lower():
                return jsonify(pokemon)
    
    # Busca por specialidade
    if pokemon_speciality:
        for pokemon in data_base_pokemon:
            if pokemon['speciality'].lower() == pokemon_speciality.lower():
                return jsonify(pokemon)


    # Se não encontrar, retorna uma mensagem de erro
    return jsonify({"error": "Pokémon não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)