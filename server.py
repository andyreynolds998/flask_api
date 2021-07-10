from flask import Flask
from data import data
import json

app = Flask(__name__)

# dictionary
me = {
    "name": "Andrew",
    "last": "Reynolds",
    "email": "andyreynolds998@gmail.com",
}

# list
products = data


@app.route("/")
@app.route("/home")
def index():
    return "Hello from Flask"


@app.route("/about")
def about():
    return me


@app.route("/about/name")
def aboutName():
    return me["name"]


@app.route("/about/fullname")
def aboutFullName():
    return me["name"] + " " + me["last"]


@app.route("/api/catalog")
def getCatalog():
    return json.dumps(products)


@app.route("/api/categories")
def getCategories():

    categories = []
    for prod in products:
        cat = prod["category "]
        if cat not in categories:
            categories.append(cat)

    return json.dumps(categories)


@app.route("/api/test")
def test():
    # add
    products.append("strawberry")
    products.append("Dragon fruit")

    # length
    # print("You have: " + str(len(products)))
    print(f"You have: {len(products)} products in your catalog")

    # iterate
    for fruit in products:
        print(fruit)

    # print an string 10 times
    for i in range(0, 10, 1):
        print(me)

    # remove apple from products
    products.remove("Apple")
    # print the list
    print(products)

    return "Check your terminal"


if __name__ == '__main__':
    app.run(debug=True)  # dont deliver to client with debugger on
