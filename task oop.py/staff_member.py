from member import Member
from book import Book

class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        print(f"Staff member {self.name} added the book '{title}' to the library.")
        return new_book 