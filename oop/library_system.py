class Book:
    def __init__(self, title: str, author: str, description: str, category: str):
        self.title = title.lower()
        self.author = author.lower()
        self.description = description.lower()
        self.category = category.lower()

    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}"
    
    def __repr__(self):
        return f"{self.title} by {self.author}"

   
class EBook(Book):
    def __init__(self, title, author, file_size: int):
        super().__init__(title, author)

        self.file_size = file_size
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)

        self.page_count = page_count

    def __str__(self):
        return f"{self.__class__.__name__}: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def check_book_shelf(self):
        if not self.books:
            print("Book Shelf is empty.")
            return 


    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def remove_book(self, title: str):
        self.check_book_shelf()
        
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"'{title}' has been removed from the library.")
                return
        
        print(f"No book found with title '{title}'.")

    def search_by_author(self, author: str):
        self.check_book_shelf()
        
        for book in self.books:
            if book.author == author:
                print(book)
                return
        print(f"No book found with title '{author}'.")

    def search_by_title(self, title: str):
        self.check_book_shelf()

        book_search_suggestions = []
        
        for book in self.books:
            if title.lower() in book.title.lower() or title.lower() in book.author.lower():
                book_search_suggestions.append(book)

        if not book_search_suggestions:
            print("No books found")
        else:
            for i in book_search_suggestions:
                print(i)

    def search_by_keyword(self, keyword: str, mode="or"):
        self.check_book_shelf()
        
        terms = [term.strip().lower() for term in keyword.split(" ")]

        results = []

        for book in self.books:
            if mode == "or":
                if any(term in book.title or term in book.author or term in book.description for term in terms):
                    results.append(book)

            else:
                if any(term in book.title and term in book.author and term in book.description for term in terms):
                    results.append(book)

        return results

    def search_by_category(self, category: str):
        self.check_book_shelf()
        
        for book in self.books:
            if category in book.category:
                print(book)
                return
            
        print(f"No book found with category '{category}'.")

    

    def search(self, *, title=None, author=None, keywords=None, category=None, mode="or"):
        self.check_book_shelf()

        results = []

        for book in self.books:
            if mode == "or":
                if any(self.search_by_title(title) or self.search_by_keyword(keywords) or self.search_by_author or self.search_by_category(category)):
                    results.append(book)
            else:
                if any(self.search_by_title(title) and self.search_by_keyword(keywords) and self.search_by_author and self.search_by_category(category)):
                    results.append(book)

        return results