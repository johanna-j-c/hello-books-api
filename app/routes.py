from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "All About Love: New Visions", "The acclaimed first volume in feminist"
#             "icon bell hooks' 'Love Song to the Nation' trilogy."),
#     Book(2, "Atomic Habits", "No matter your goals, Atomic Habits offers a proven" 
#             "framework for improving - every day."),
#     Book(3, "Milk and Honey", "a collection of poetry and prose about survival." 
#             "About the experience of violence, abuse, love, loss, and femininity.")
# ]

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book(title=request_body["title"],
                description=request_body["description"])
    
    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)


@books_bp.route("", methods=["GET"])
def handle_books():
    books = Book.query.all()
    book_response = []

    for book in books:
        book_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })

    return jsonify(book_response)

def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"Book {book.id} is invalid"}, 400))
    
    book = Book.query.get(book_id)

    if not book:
        abort(make_response({"message":f"Book {book.id} not found"}, 404))
    
    return book

@books_bp.route("/<book_id>", methods=["GET"])
def get_one_book(book_id):
    book = validate_book(book_id)

    return {
        "title": book.title,
        "description": book.description
    }

# def validate_book(book_id):
#     try:
#         book_id = int(book_id) 
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))
    
#     for book in books:
#         if book.id == book_id:
#             return book
    
#     abort(make_response({"message":f"book {book_id} not found"}, 404))

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
    
#     book = validate_book(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description
#     }