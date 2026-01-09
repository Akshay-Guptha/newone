class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"[{self.isbn}] {self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book.title}")

    def show_all_books(self):
        print("\n--- Library Catalog ---")
        for book in self.books:
            print(book)
        print("-----------------------\n")

    def lend_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_available:
                    book.is_available = False
                    print(f"Success! You have borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already checked out.")
                    return
        print("Error: Book with that ISBN not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.is_available = True
                print(f"Success! You have returned '{book.title}'.")
                return
        print("Error: Invalid ISBN.")


# --- Simple CLI Menu to interact with the system ---
def main():
    my_library = Library()
    
    # Pre-populating with some books
    my_library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "101"))
    my_library.add_book(Book("1984", "George Orwell", "102"))
    my_library.add_book(Book("The Hobbit", "J.R.R. Tolkien", "103"))

    while True:
        print("\n1. Display Books\n2. Borrow Book\n3. Return Book\n4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            my_library.show_all_books()
        elif choice == "2":
            isbn = input("Enter ISBN to borrow: ")
            my_library.lend_book(isbn)
        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            my_library.return_book(isbn)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid selection, try again.")

if __name__ == "__main__":
    main()