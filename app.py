from flask import Flask

app = Flask(__name__)

stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

@app.route("/")
def home():
    return "Welcome to the store API"

@app.get("/store")
def get_stores():
    return {"stores": stores}
