
from flask import Flask, jsonify, request
from pymongo import MongoClient
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Replace 'mongodb://localhost:27017' with your MongoDB connection string
client = MongoClient('mongodb://localhost:27017')

# Swagger UI configuration
swaggerui_blueprint = get_swaggerui_blueprint(
    '/swagger',
    '/static/swagger.json',
    config={
        'url': '/static/swagger.json'
    }
)

app.register_blueprint(swaggerui_blueprint)

@app.route('/static/swagger.json')
def swagger_spec():
    spec = {
        "swagger": "2.0",
        "info": {
            "title": "MongoDB API",
            "version": "1.0.0",
            "description": "API for interacting with MongoDB collections"
        },
        "paths": {
            "/api/data/{collection_name}/search": {
                "get": {
                    "summary": "Search data in a collection",
                    "description": "Searches for data based on a key-value pair and regular expression.",
                    "parameters": [
                        {
                            "name": "collection_name",
                            "in": "path",
                            "required": True,
                            "type": "string",
                            "description": "The name of the collection"
                        },
                        {
                            "name": "key",
                            "in": "query",
                            "required": True,
                            "type": "string",
                            "description": "The key to search for"
                        },
                        {
                            "name": "value",
                            "in": "query",
                            "required": True,
                            "type": "string",
                            "description": "The value to search for"
                        },
                        {
                            "name": "limit",
                            "in": "query",
                            "required": False,
                            "type": "integer",
                            "description": "Limit the number of results"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Success",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "object"
                                }
                            }
                        },
                        "400": {
                            "description": "Bad Request"
                        },
                        "500": {
                            "description": "Internal Server Error"
                        }
                    }
                }
            },
            "/api/data/{collection_name}/filter": {
                "get": {
                    "summary": "Filter data in a collection",
                    "description": "Filters data based on multiple criteria.",
                    "parameters": [
                        {
                            "name": "collection_name",
                            "in": "path",
                            "required": True,
                            "type": "string",
                            "description": "The name of the collection"
                        },
                        {
                            "name": "key",
                            "in": "query",
                            "required": False,
                            "type": "string",
                            "description": "The key to filter by"
                        },
                        {
                            "name": "value",
                            "in": "query",
                            "required": False,
                            "type": "string",
                            "description": "The value to filter by"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Success",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "object"
                                }
                            }
                        },
                        "400": {
                            "description": "Bad Request"
                        },
                        "500": {
                            "description": "Internal Server Error"
                        }
                    }
                }
            },
            "/api/data/{collection_name}/all": {
                "get": {
                    "summary": "Get all data from a collection",
                    "description": "Retrieves all data from the specified collection.",
                    "parameters": [
                        {
                            "name": "collection_name",
                            "in": "path",
                            "required": True,
                            "type": "string",
                            "description": "The name of the collection"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Success",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "object"
                                }
                            }
                        },
                        "400": {
                            "description": "Bad Request"
                        },
                        "500": {
                            "description": "Internal Server Error"
                        }
                    }
                }
            },
            "/api/data/{collection_name}/text_search": {
                "get": {
                    "summary": "Text search in a collection",
                    "description": "Searches for text within the specified collection.",
                    "parameters": [
                        {
                            "name": "collection_name",
                            "in": "path",
                            "required": True,
                            "type": "string",
                            "description": "The name of the collection"
                        },
                        {
                            "name": "text",
                            "in": "query",
                            "required": True,
                            "type": "string",
                            "description": "The text to search for"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "Success",
                            "schema": {
                                "type": "array",
                                "items": {
                                    "type": "object"
                                }
                            }
                        },
                        "400": {
                            "description": "Bad Request"
                        },
                        "500": {
                            "description": "Internal Server Error"
                        }
                    }
                }
            }
        }
    }

    return jsonify(spec)

@app.route('/api/data/<collection_name>/search', methods=['GET'])
def search_data(collection_name):
    try:
        db = client[collection_name.split('_')[0]]
        collection = db[collection_name]

        key = request.args.get('key')
        value = request.args.get('value')

        if key and value:
            # Use regular expression search
            results = collection.find({key: {'$regex': value, '$options': 'i'}})

            # Check if the 'limit' parameter is present
            if 'limit' in request.args:
                limit = int(request.args.get('limit'))
                results = results.limit(limit)

            return jsonify(list(results))
        else:
            return jsonify({'error': 'Missing key or value parameter'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/data/<collection_name>/filter', methods=['GET'])
def filter_data(collection_name):
    try:
        db = client[collection_name.split('_')[0]]
        collection = db[collection_name]

        filters = {}
        for key in request.args:
            if key != 'collection_name':
                filters[key] = request.args.get(key)

        results = collection.find(filters)
        return jsonify(list(results))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/data/<collection_name>/all', methods=['GET'])
def get_all_data(collection_name):
    try:
        db = client[collection_name.split('_')[0]]
        collection = db[collection_name]

        all_data = collection.find()
        return jsonify(list(all_data))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/data/<collection_name>/text_search', methods=['GET'])
def text_search(collection_name):
    try:
        db = client[collection_name.split('_')[0]]
        collection = db[collection_name]

        text = request.args.get('text')

        if text:
            # Create a text index if it doesn't exist
            collection.create_index([('name', 'text'), ('value', 'text')], name='text_index')

            results = collection.find({'$text': {'$search': text}})
            return jsonify(list(results))
        else:
            return jsonify
          
if __name__ == '__main__':
    app.run(debug=True)
