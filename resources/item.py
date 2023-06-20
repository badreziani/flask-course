from uuid import uuid4
from flask import request
from flask_smorest import abort, Blueprint
from flask.views import MethodView
from db import items

blp = Blueprint("items", __name__, description="Item endpoints.")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message="Item not found.")

    def put(self, item_id):
        data = request.json()

        try:
            item = items[item_id]
            item |= data
            return item
        except KeyError:
            abort(404, message="Item not found.")


@blp.route("/item")
class ItemList(MethodView):
    def get(self):
        return {"items": list(items.values())}

    def post(self):
        data = request.get_json()
        if data["store_id"] not in stores:
            abort(404, message="Store not found.")

        item_id = uuid4().hex
        item = {"id": item_id, **data}
        items[item_id] = item
        return item, 201
