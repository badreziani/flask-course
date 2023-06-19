import uuid
from flask import Flask, request
from flask_smorest import abort
from db import stores, items
app = Flask(__name__)


@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    data = request.get_json()
    store_id = uuid.uuid4().hex
    new_store = {"id": store_id, **data}
    stores[store_id] = new_store
    print(new_store)
    return new_store, 201


@app.get("/store/<string:store_id>")
def get_store(store_id: str):
    try:
        return stores[store_id]
    except KeyError:
        return {"details": "Store not found"}, 404


@app.get("/item")
def get_store_items():
    data = request.get_json()
    if data["store_id"] not in stores:
        return {"details": "Store not found"}, 404
    item_id = uuid.uuid4().hex
    new_item = {"id": item_id, **data}
    items[item_id] = new_item
    return new_item, 201
