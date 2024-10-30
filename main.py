# main.py
from src.models import Book, Magazine, Member
from src.services.library import Library

def main():
    # Create library instance
    library = Library()
    
    # Add sample data
    book1 = Book("Python Programming", "John Smith", "978-1234567890", 400)
    magazine1 = Magazine("Tech Weekly", "Various Authors", "2024-Issue-1")
    member1 = Member("Alice Brown", "alice@email.com")
    
    # Add items and member to library
    library.add_item(book1)
    library.add_item(magazine1)
    library.add_member(member1)
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Magazine")
        print("3. Add Member")
        print("4. Borrow Item")
        print("5. Return Item")
        print("6. List Available Items")
        print("7. List Member Items")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            pages = int(input("Enter number of pages: "))
            book = Book(title, author, isbn, pages)
            library.add_item(book)
            
        elif choice == "2":
            title = input("Enter magazine title: ")
            author = input("Enter author/publisher: ")
            issue = input("Enter issue number: ")
            magazine = Magazine(title, author, issue)
            library.add_item(magazine)
            
        elif choice == "3":
            name = input("Enter member name: ")
            email = input("Enter member email: ")
            member = Member(name, email)
            library.add_member(member)
            
        elif choice == "4":
            library.list_available_items()
            item_id = input("Enter item ID to borrow: ")
            library.list_members()
            member_id = input("Enter member ID: ")
            try:
                library.borrow_item(item_id, member_id)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "5":
            item_id = input("Enter item ID to return: ")
            try:
                library.return_item(item_id)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "6":
            library.list_available_items()
            
        elif choice == "7":
            library.list_members()
            member_id = input("Enter member ID: ")
            try:
                library.list_member_items(member_id)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == "8":
            print("Thank you for using the Library Management System!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()