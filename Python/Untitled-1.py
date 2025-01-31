class Library:
    def __init__(self):
        self. books = {
            "Fanatical About Frogs": "F. Scott Fitzgerald",
            "1984": "George Orwell",
            "To Kill a Mockingbird": "Harper Lee",
            "Heart in Hand": "J.D. Salinger",
            "Pride and Prejudice": "Jane Austen",
            "The Forgotten": "J.R.R. Tolkien",
            "Blood Red": "Herman Melville",
            "War and Peace": "Leo Tolstoy",
        }
        
        self. borrowed_books = []
        
    def view_books (self):
        print ("Available Books:")
        for title, author in self.books.items ():
            avaliable = "yes" if title not in self.borrowed_books else "no"
            print (f"Title: {title}, Author: {author}, avaliable: {avaliable}\n")
            
    def borrow_book (self, title):
        if title in self.books:
            if title not in self.borrowed_books:
                self.borrowed_books.append (title)
                print (f"You have borrowed '{title}'.")
            else:
                print (f"Sorry, '{title}' is already borrowed.")
        else:
            print (f"Sorry, '{title}' is not in the library.")

    def return_book (self, title):
        if title in self. books:
            if title in self.borrowed_books:
                self. borrowed_books. remove(title)
                print (f"You have returned '{title}'.")
            else:
                print(f"'{title}' was not borrowed.")
        else:
            print(f"'{title}' is not recognized.")

def main ():
    library = Library ()
    
    while True:
        print ("Welcome to Library")
        print ()
        print ("Make a choice: ")
        print ("1. View Books")
        print ("2. Borrow Book")
        print ("3. Return Book")
        print ()
        i= input ("Choose an option: ")
        if i == '1':
            library. view_books ()
        elif i == '2':
            title = input ("Enter the title of the book to borrow: ")
            library. borrow_book(title)
        elif i == '3':
            title = input ("Enter the title of the book to return: ")
            library.return_book(title)
        else:
            print ("Invalid choice. Please try again.")

if __name__ == "__main__":
    main ()
