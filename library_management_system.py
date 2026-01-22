books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn
    }

    books.append(book)
    print("Book added successfully!\n")

def view_books():
    if not books:
        print("No books available.\n")
        return

    for book in books:
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"ISBN: {book['isbn']}")
        print("----------------------")

def search_book():
    isbn = input("Enter ISBN to search: ")
    for book in books:
        if book["isbn"] == isbn:
            print("Book Found:")
            print(book)
            return
    print("Book not found.\n")

def main_menu():
    while True:
        print("LIBRARY MANAGEMENT SYSTEM")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

main_menu()