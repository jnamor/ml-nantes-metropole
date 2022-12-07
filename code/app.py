from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from ressources.item import Item
from ressources.item import ItemList


app = Flask(__name__)
app.secret_key = 'keepthissecret'
api = Api(app)
CORS(app)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


if __name__ == '__main__':
    app.run(debug=True)