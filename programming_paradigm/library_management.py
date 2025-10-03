class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
    
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return False
        return True

    def __str__(self):
        return f"{self.title} by {self.author}"

    
class Library:
    def __init__(self):
        self._books = []


    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        if not self._books:
            print("Book Library is empty.")
            return
        
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    print(f"\nYou have successfully checked out '{book.title}")
                    return
                else:
                    print(f"\n'{book.title}' is already checked out.")
                    return
        print(f"\nBook titled '{title}' not found in the library.")

    def return_book(self, title):
        if not self._books:
            print("Book Library is empty.")
            return
        
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    print(f"\n'{book.title}' has been returned successfully.")
                    return
                else:
                    print(f"\n'{book.title}' was not checked out.")
                    return
                
        print(f"\nBook titled '{title}' not found in the library.")
        

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if not available_books:
            print("Book Library is empty.")
        for book in available_books:
            print(f"{book}")

