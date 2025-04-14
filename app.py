import os

def load_library(filename="library.txt"):
    """Load library data from file when program starts"""
    books = []
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 5:
                        books.append({
                            "title": parts[0],
                            "author": parts[1],
                            "year": int(parts[2]),
                            "genre": parts[3],
                            "read": parts[4] == "True"
                        })
            print("\nLibrary loaded successfully from previous session!")
        except Exception as e:
            print(f"\nError loading library: {e}")
    return books

def save_library(books, filename="library.txt"):
    """Save library data to file when program exits"""
    try:
        with open(filename, "w") as f:
            for book in books:
                f.write(f"{book['title']}|{book['author']}|{book['year']}|"
                        f"{book['genre']}|{book['read']}\n")
        print("\nLibrary saved successfully!")
    except Exception as e:
        print(f"\nError saving library: {e}")

def library():
    books = load_library()  # Load existing data on startup
    
    try:
        while True:
            print("\n===== Library Menu =====")
            print("1. Add a new book")
            print("2. View all books")
            print("3. Search for a book")
            print("4. Mark a book as read/unread")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ")
            
            if choice == "1":
                print("\n--- Add New Book ---")
                book = {
                    "title": input("Title: ").strip().title(),
                    "author": input("Author: ").strip().title(),
                    "year": int(input("Publication Year: ")),
                    "genre": input("Genre: ").strip().capitalize(),
                    "read": input("Have you read this book? (yes/no): ").lower() == "yes"
                }
                books.append(book)
                print(f"\n'{book['title']}' has been added to the library!")
                
            elif choice == "2":
                print("\n--- All Books ---")
                if not books:
                    print("The library is empty.")
                else:
                    for i, book in enumerate(books, 1):
                        read_status = "✓" if book["read"] else "✗"
                        print(f"{i}. {book['title']} by {book['author']} ({book['year']})")
                        print(f"   Genre: {book['genre']} | Read: {read_status}\n")
                        
            elif choice == "3":
                print("\n--- Search Books ---")
                search_term = input("Enter title or author to search: ").lower()
                found = [b for b in books 
                         if search_term in b["title"].lower() or search_term in b["author"].lower()]
                
                if not found:
                    print("No matching books found.")
                else:
                    print(f"\nFound {len(found)} matching book(s):")
                    for i, book in enumerate(found, 1):
                        print(f"{i}. {book['title']} by {book['author']}")
                        
            elif choice == "4":
                print("\n--- Mark Read/Unread ---")
                if not books:
                    print("The library is empty.")
                    continue
                    
                for i, book in enumerate(books, 1):
                    print(f"{i}. {book['title']}")
                    
                try:
                    book_num = int(input("Enter book number: ")) - 1
                    if 0 <= book_num < len(books):
                        books[book_num]["read"] = not books[book_num]["read"]
                        status = "read" if books[book_num]["read"] else "unread"
                        print(f"'{books[book_num]['title']}' marked as {status}!")
                    else:
                        print("Invalid book number.")
                except ValueError:
                    print("Please enter a valid number.")
                    
            elif choice == "5":
                print("\nSaving your library...")
                save_library(books)  # Save before exiting
                print("Goodbye!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1-5.")
    
    except KeyboardInterrupt:
        print("\n\nEmergency save triggered!")
        save_library(books)
        print("Goodbye!")

if __name__ == "__main__":
    library()