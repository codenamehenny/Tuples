#2. Python Data Structure Challenges in Real-World Scenarios
#Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
 
# this function checks if input is in library before adding it
def add_book(title, author):
    book_pair = (title, author)
    if book_pair not in library:
        library.append(book_pair) #adds the tuple to the library list
        print(f"'{book_pair[0]}' by {book_pair[1]} has been added")
        return library
    elif book_pair in library:
        print(f"\nDuplicate error, {book_pair[0]} by {book_pair[1]} is already in library") 

# main function to choose whether to add a book, show inventory or quit
def library_menu():
    while True:
        print("\nWelcome to the Library!")
        print("1. Add book \n2. Inventory \n3. Quit")
        try:
            option = int(input("Enter option number: "))
            if option == 1:
                title = input("Enter the book's title: ")
                author = input("Enter the author's name: ")
                add_book(title, author)
            elif option == 2:
                print("\nHere's the available books in the library:")
                for book in library:
                    print(f"'{book[0]}' by {book[1]}")  # title at index 0 and author at index 1
            elif option == 3:
                break
        except ValueError:
            print("Invalid input, please try again.")

library_menu()