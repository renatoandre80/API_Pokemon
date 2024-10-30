
# Pokémon API

Esta é uma API simples em Flask que permite buscar informações de Pokémon usando query parameters. A API consulta uma base de dados local chamada `data_base_pokemon`.

## Pré-requisitos

- Python 3.x
- Flask

## Requirements

- Basta rodar no terminal : pip install -r requirements.txt

## como testar a implementação:

Endpoints
GET /pokemon
Este endpoint busca informações sobre um Pokémon com base em parâmetros de consulta (query parameters). Ele permite a busca de um Pokémon específico por id, name, ou speciality.

Query Parameters Disponíveis
id: O ID numérico do Pokémon.
name: O nome do Pokémon.
speciality: A especialidade ou tipo do Pokémon (exemplo: Electric, Fire, etc.).
Nota: Apenas um parâmetro de consulta é avaliado por vez, com a seguinte prioridade: id → name → speciality.

Exemplos de Uso
1. Buscar por ID
Para buscar um Pokémon pelo seu id, adicione o id como um parâmetro de consulta. Por exemplo, para buscar o Pokémon com id=1:


exemplo:
GET http://127.0.0.1:5000/pokemon?id=1