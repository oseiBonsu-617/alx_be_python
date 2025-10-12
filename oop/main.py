from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen", "A Beautiful love Story", "Romance")
    # digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    # paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    # classic_book1 = Book("Pride and Prejudice 2", "Jane Austen")
    # classic_book2 = Book("Snow white and Prejudice", "Jane Austen")

    # Add books to the library
    my_library.add_book(classic_book)
    # my_library.add_book(classic_book1)
    # my_library.add_book(classic_book2)
    # my_library.add_book(digital_novel)
    # my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

    # # Remove one book from the library
    my_library.remove_book("Pride and Prejudice")

    # #List all books in the Library
    # my_library.list_books()

    # # Search for a book in the library
    # my_library.search_book("Jane Austen")

    # my_library.search_by_title("Snow")

if __name__ == "__main__":
    main()