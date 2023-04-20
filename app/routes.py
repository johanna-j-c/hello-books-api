from flask import Blueprint

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