from flask import Flask, request, jsonify
from Library.LibraryFacade import LibraryFacade

app = Flask(__name__)

# @app.errorhandler(Exception)
# def handle_exception(error):
#     # Create a default response
#     print(error)
#     response = {
#         "error": "An unexpected error occurred.",
#         "message": str(error)
#     }
#     return jsonify(response), 500

facade = LibraryFacade()


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


if __name__ == '__main__':
    app.run(port=3000)
