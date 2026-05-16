# Dictionary to store books: {book_id: {"title": title, "available": True}}
library_books = {}  

# Functionality 1: Add a Book
def add_book(book_id, title):
    # If-else condition to check if book already exists
    if book_id in library_books:
        return False, "Book ID already exists."
    
    library_books[book_id] = {"title": title, "available": True}
    return True, f"Book '{title}' added successfully."

# Functionality 2: View All Books
def view_books():
    # If-else condition
    if not library_books:
        return "No books in the library."
    
    book_list = ""
    # For loop to iterate through books
    for b_id, details in library_books.items():
        status = "Available" if details["available"] else "Borrowed"
        book_list += f"ID: {b_id} | Title: {details['title']} | Status: {status}\n"
    
    return book_list.strip()

# Functionality 3: Borrow a Book
def borrow_book(book_id):
    if book_id not in library_books:
        return False, "Book not found."
    if not library_books[book_id]["available"]:
        return False, "Book is already borrowed."
    
    library_books[book_id]["available"] = False
    return True, f"You have successfully borrowed '{library_books[book_id]['title']}'."

# Functionality 4: Return a Book
def return_book(book_id):
    if book_id not in library_books:
        return False, "Book not found."
    if library_books[book_id]["available"]:
        return False, "Book was not borrowed."
    
    library_books[book_id]["available"] = True
    return True, f"You have successfully returned '{library_books[book_id]['title']}'."

# User Interface (CLI Menu)
def main_menu():
    # While loop for continuous menu execution
    while True:
        print("\n--- Library Management System ---")
        print("1. Add a Book")
        print("2. View All Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            b_id = input("Enter Book ID (e.g., 101): ")
            title = input("Enter Book Title: ")
            success, msg = add_book(b_id, title)
            print(msg)
            
        elif choice == '2':
            print("\n--- Book List ---")
            print(view_books())
            
        elif choice == '3':
            b_id = input("Enter Book ID to borrow: ")
            success, msg = borrow_book(b_id)
            print(msg)
            
        elif choice == '4':
            b_id = input("Enter Book ID to return: ")
            success, msg = return_book(b_id)
            print(msg)
            
        elif choice == '5':
            print("Exiting system...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()