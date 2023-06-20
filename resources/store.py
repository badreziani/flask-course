from uuid import uuid4
from flask import request
from flask_smorest import abort, Blueprint
from flask.views import MethodView
from db import stores

blp = Blueprint("stores", __name__, description="Store endpoints")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found.")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message="Store not found.")


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}

    def post(self):
        data = request.get_json()
        if "name" not in data:
            abort(400, message="Bad request. Name required.")
            
        for store in stores.values():
            if data["name"] == store["name"]:
                abort(400, message="Store already exists.")
                
        store_id = uuid4().hex
        store = {"id": store_id, **data}
        stores[store_id] = store
        return store, 201
