from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "Oryava",
        "items": [
            {"name": "Gomme dépilatoire", "price": 19.99},
            {"name": "Power bank", "price": 22.99}
        ]
    },
]


@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    data = request.get_json()
    new_store = {**data}
    print(new_store)
    return new_store, 201


@app.get("/store/<string:name>")
def get_store(name: str):
    store = [s for s in stores if s["name"] == name][0]
    if store:
        return store
    return {"details": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_store_items(name: str):
    store = [s for s in stores if s["name"] == name][0]
    if store:
        return store["items"]
    return {"details": "Store not found"}, 404
