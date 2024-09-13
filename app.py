from flask import Flask, request

app = Flask(__name__)


stores = {}
items = {
    1:{},
    2:{}
}

@app.route("/")
def home():
    return "Welcome to the store API"

@app.get("/store")
def get_stores():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data = request.get_json()
    print(f"{request_data} \n\n\n")
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")  # Crocodile tags are for dynamic segments in a url  data type: variable name
def create_item(name: str):
    request_data = request.get_json()
    for obj in stores:
        if name == obj["name"]:
            new_item = {"name": request_data["name"], "price": request_data["cost"]}
            obj["items"].append(new_item)
            #  return new_item, 201, "Successfully achieved"
            return new_item, 201

    # In case we don't find the name
    return "Message: We didn't find the store", 404

