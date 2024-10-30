data_base_pokemon=[
    {"id": 1, "name": "Bulbasaur", "speciality": "Grass/Poison"},
    {"id": 2, "name": "Ivysaur", "speciality": "Grass/Poison"},
    {"id": 3, "name": "Venusaur", "speciality": "Grass/Poison"},
    {"id": 4, "name": "Charmander", "speciality": "Fire"},
    {"id": 5, "name": "Charmeleon", "speciality": "Fire"},
    {"id": 6, "name": "Charizard", "speciality": "Fire/Flying"},
    {"id": 7, "name": "Squirtle", "speciality": "Water"},
    {"id":8,"name":'Pikachu','speciality':'Electric'}
]

for elemento in data_base_pokemon:
    print(elemento['id'],elemento['name'],elemento['speciality'])