import json
import os

# File to store the library data
LIBRARY_FILE = "library.txt"

def load_library():
    """Load the library from a file if it exists."""
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    """Save the library to a file."""
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file)

def add_book(library):
    """Add a book to the library."""
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status,
    }
    library.append(book)
    print(f"Book '{title}' added successfully!")

def remove_book(library):
    """Remove a book from the library by title."""
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print(f"Book '{title}' removed successfully!")
            return
    print(f"Book '{title}' not found in the library.")

def search_books(library):
    """Search for books by title or author."""
    search_term = input("Enter a title or author to search for: ").lower()
    results = [
        book
        for book in library
        if search_term in book["title"].lower() or search_term in book["author"].lower()
    ]
    if results:
        print("\nSearch Results:")
        for book in results:
            print_book(book)
    else:
        print("No matching books found.")

def display_all_books(library):
    """Display all books in the library."""
    if not library:
        print("The library is empty.")
    else:
        print("\nAll Books:")
        for book in library:
            print_book(book)

def print_book(book):
    """Print a single book's details in a formatted way."""
    status = "Read" if book["read_status"] else "Unread"
    print(
        f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Status: {status}"
    )

def display_statistics(library):
    """Display library statistics."""
    total_books = len(library)
    read_books = sum(book["read_status"] for book in library)
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    print("\nLibrary Statistics:")
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main_menu():
    """Display the main menu and handle user input."""
    library = load_library()

    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()