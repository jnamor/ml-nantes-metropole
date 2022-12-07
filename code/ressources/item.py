from flask_restful import Resource
from models.item import ItemModel


class Item(Resource):
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item
        return {'message': 'Item not found.'}, 404


class ItemList(Resource):
    def get(self):
        data = ItemModel.find_all()
        return {'items': data}