import uuid
from flask import Flask, request
from flask_smorest import abort
from db import stores, items
app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id: str):
    try:
        return stores[store_id]
    except KeyError:
        abort(404, message="Store not found.")


@app.post("/store")
def create_store():
    data = request.get_json()
    store_id = uuid.uuid4().hex
    store = {"id": store_id, **data}
    stores[store_id] = store
    return store, 201


@app.get("/item/<string:item_id>")
def get_stores(item_id: str):
    try:
        return stores[item_id]
    except KeyError:
        abort(404, message="Item not found.")


@app.post("/item")
def create_item():
    data = request.get_json()
    if data["store_id"] not in stores:
        abort(404, message="Store not found.")

    item_id = uuid.uuid4().hex
    item = {"id": item_id, **data}
    items[item_id] = item
    return item, 201


@app.get("/item")
def get_items():
    return {"items": list(items.values())}
