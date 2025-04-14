def library():
    books = []
    
    while True:
        print("\n===== Library Menu =====")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Search for a book")
        print("4. Mark a book as read/unread")
        print("5. Save library to file")
        print("6. Load library from file")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            # Add a new book
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
            # View all books
            print("\n--- All Books ---")
            if not books:
                print("The library is empty.")
            else:
                for i, book in enumerate(books, 1):
                    read_status = "✓" if book["read"] else "✗"
                    print(f"{i}. {book['title']} by {book['author']} ({book['year']})")
                    print(f"   Genre: {book['genre']} | Read: {read_status}\n")
                    
        elif choice == "3":
            # Search for a book
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
            # Mark as read/unread
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
            # Save to file
            try:
                with open("library.txt", "w") as f:
                    for book in books:
                        f.write(f"{book['title']}|{book['author']}|{book['year']}|"
                                f"{book['genre']}|{book['read']}\n")
                print("Library saved successfully!")
            except Exception as e:
                print(f"Error saving file: {e}")
                
        elif choice == "6":
            # Load from file
            try:
                with open("library.txt", "r") as f:
                    books.clear()
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
                print("Library loaded successfully!")
            except FileNotFoundError:
                print("No saved library found.")
            except Exception as e:
                print(f"Error loading file: {e}")
                
        elif choice == "7":
            # Exit
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1-7.")

if __name__ == "__main__":
    library()
   
