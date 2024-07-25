from flask import Flask, request, jsonify
from Library.LibraryFacade import LibraryFacadeSingleton

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_exception(error):
    print(error)
    response = {
        "error": "An unexpected error occurred.",
        "message": str(error)
    }
    return jsonify(response), 500


facade = LibraryFacadeSingleton


@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"


@app.route('/api/books', methods=['GET'])
def get_all_books():
    return jsonify(facade.find_all_Books())


@app.route('/api/books', methods=['POST'])
def register_book():
    request_data = request.get_json()
    title = request_data["title"]
    author = request_data["author"]
    category = request_data["category"]
    facade.add_book(title, author, category)
    return jsonify({"response": "book successfuly saved"}), 201


@app.route('/api/books/find/<query>', methods=['GET'])
def search_books(query):
    response = facade.search_books(query)
    return jsonify(response), 201


@app.route('/api/users', methods=['POST'])
def register_user():
    request_data = request.get_json()
    user_id = request_data["user_id"]
    name = request_data["name"]
    user_type = request_data["user_type"]
    facade.add_user(user_id, name, user_type)
    return jsonify({"response": "user successfuly saved"}), 201


@app.route('/api/users/find/<user_id>', methods=['GET'])
def search_user(user_id):
    user = facade.find_user(user_id)
    response = {
        "user_id": user.user_id,
        "name": user.name,
        "user_type": user.user_type
    }
    return jsonify(response), 201


@app.route('/api/users/history/<user_id>', methods=['GET'])
def get_user_history(user_id):
    response = facade.get_user_history(user_id)
    return jsonify(response), 201


@app.route('/api/borrow/', methods=['POST'])
def borrow_book():
    request_data = request.get_json()
    user_id = request_data["user_id"]
    title = request_data["title"]
    facade.borrow_book(user_id, title)
    return jsonify({"response": "borrow request successfuly saved"}), 201


@app.route('/api/return/', methods=['POST'])
def return_book():
    request_data = request.get_json()
    user_id = request_data["user_id"]
    title = request_data["title"]
    facade.return_book(user_id, title)
    return jsonify({"response": "return request successfuly saved"}), 201


if __name__ == '__main__':
    app.run(port=3000)
