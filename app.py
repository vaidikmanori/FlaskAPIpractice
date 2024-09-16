import uuid
from flask import Flask, request
from db import items, stores


app = Flask(__name__)




items.values()

@app.route("/")
def home():
    return "Welcome to the store API"

@app.get("/store")
def get_stores():
    return {"stores": list(stores.values())}


@app.post("/store")
def create_store():
    store_data = request.get_json()
    store_id = uuid.uid4().hex
    # print(f"{request_data} \n\n\n")
    new_store = {**store_data, "id": store_id}
    stores[store_id] = new_store
    return new_store, 201


@app.post("/item")  # Crocodile tags are for dynamic segments in a url  data type: variable name
def create_item():
    item_data = request.get_json()
    if item_data["store_id"] not in stores:
        # In case item is not there
        return {"Message": "Store NOT Found"}, 404
    else:
        item_id = uuid.uid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item

        return item, 201


@app.get("/item")
def get_all_items():
    return {"items": list(items.values())}


@app.get("/store/<string:store_id>")
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Id not found."}, 404


@app.get("/item/<string:item_id>")
def get_item(name):
    try:
        return item[item_id]
    except KeyError:
        return {"Message": "Item NOT Found"}, 404