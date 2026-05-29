class Book:

    """
    1. Complete the Book Class

        1. Complete the __init__(self, title, author) method
            1. Set .title and .author to the values of the parameters
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    """
    2. Complete the Library Class:
    """
class Library:

    """
        1. Complete the __init__(self, name) method
            1. Initialize a .name member variable to the value of the name parameter
            2. Create a .books member initialized to an empty list
    """
    def __init__(self, name):
        self.name = name
        self.books = []

    """
    3. Complete the add_book(self, book) method:
        1. Add book, the given Book instance, to the library's books instance variable by appending it to the end of the list
    """
    def add_book(self, book):
        self.books.append(book)

    """
    4. Complete the remove_book(self, book) method:
        1. Create a new, empty list to hold the books you want to keep
        2. Loop through every book in the library's books list
            1. If either the book's title or author doesn't match the one you want to remove, add it to the new list
            2. After checking all the books, replace the library's books list with the new list
    """
    def remove_book(self, book):
        new_books = []
        for b in self.books:
            if b.title != book.title or b.author != book.author:
                new_books.append(b)
        self.books = new_books

    """
    5. Complete the search_books(self, search_string) method:
        1. For every book in the library check if the search_string is contained in the title or author field (case-insensitive)
        2. Return a list of all books that match the search string, ordered in the same order as they were added to the library
    """
    def search_books(self, search_string):
        search_string = search_string.lower()
        matching_books = []
        for book in self.books:
            if search_string in book.title.lower() or search_string in book.author.lower():
                matching_books.append(book)
        return matching_books

if __name__ == "__main__":
    # Create a library
    my_library = Library("My Library")

    # Create some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")

    # Add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # Search for books containing "the"
    search_results = my_library.search_books("the")
    print("Search results for 'the':")
    for book in search_results:
        print(f"{book.title} by {book.author}")

    # Remove a book and search again
    my_library.remove_book(book1)
    search_results = my_library.search_books("the")
    print("\nSearch results for 'the' after removing 'The Great Gatsby':")
    for book in search_results:
        print(f"{book.title} by {book.author}")