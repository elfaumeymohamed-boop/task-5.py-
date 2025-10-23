class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn  # خاص (Encapsulated)
        self.available = True

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.__isbn}")
        print(f"Available: {'Yes' if self.available else 'No'}")

    # Getter and Setter for ISBN
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn