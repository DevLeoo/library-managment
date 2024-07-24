from flask import Flask, request, jsonify

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


@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"


@app.route('/api/book', methods=['GET'])
def get_all_books():
    df = pd.read_csv("./persistance/books.csv")
    return jsonify(df.to_dict(orient='records'))


app.route('/api/book/loan', methods=['POST'])


def rent_book():
    # data = {"title": "1984"}
    data = request.json
    user = User("John Doe", 1)

    lib_facade = LibraryFacade()
    lib_facade.loan_book(data["title"], user)

    return jsonify({"name": "successfuly rented"}), 201


if __name__ == '__main__':
    app.run(port=3000)
