from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "All About Love: New Visions", "The acclaimed first volume in feminist"
            "icon bell hooks' 'Love Song to the Nation' trilogy."),
    Book(2, "Atomic Habits", "No matter your goals, Atomic Habits offers a proven" 
            "framework for improving - every day."),
    Book(3, "Milk and Honey", "a collection of poetry and prose about survival." 
            "About the experience of violence, abuse, love, loss, and femininity.")
]

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    book_response = []
    for book in books:
        book_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(book_response)