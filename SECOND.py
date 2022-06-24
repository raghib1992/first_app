from flask import Flask, jsonify, request

app = Flask(__name__)

books_db = [
    {
        "name": "Secret",
        "price": 250
    
    },
    {
        "name": "Harry potter",
        "price": 350
    
    },
    {
        "name": "Secret",
        "price": 250
    
    },
    {
        "name": "The Lord of the Ring",
        "price": 320
    
    }
]

# Retrieve all the books
@app.route("/books")
def get_all_books():
    return jsonify({"books": books_db})


# Retrive one book
@app.route("/book/<string:name>")
def get_book(name):
    for book in books_db:
        if book['name'] == name:
            return jsonify(book)
    return jsonify({"message": "book n0t found"})

# Create a book
@app.route("/book", methods=["POST"])
def create_book():
    body_data = request.get_json()
    books_db.append(body_data)
    return jsonify({"message": "New Book created"})

app.run(port=5000)