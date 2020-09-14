import sqlite3


#Book class for the books
class Book():

    #Features of the book
    def __init__(self,author,name,totalpages):

        self.author = author
        self.name = name
        self.totalpages = totalpages

    #We're going to take the features as a output. So We should return them.
    def __str__(self):
        return "\nAuthor: {} \nName: {} \nTotal Pages: {}\n".format(self.author,self.name,str(self.totalpages))



#This the library.
#This class contain the whole data of the program and whole functions that we're going to use during the processes
class Library():

    def __init__(self):

        self.make_connection()

    #Making connection between the program and the database
    def make_connection(self):

        self.connection = sqlite3.connect("../DataBase/Library.db")

        self.cursor = self.connection.cursor()

        query = "CREATE TABLE IF NOT EXISTS Library(Author TEXT,Name TEXT,Total Pages INTEGER)"

        self.cursor.execute(query)

        self.connection.commit()

    #Shutting down the database
    def disconnect(self):

        self.connection.close()

    #Listing the all books
    def list_books(self):
        
        query = "SELECT * FROM Library"

        self.cursor.execute(query)

        books = self.cursor.fetchall()

        if (len(books) == 0):
            print("It seems empty.")
            return 1
        
        else:
            
            for i in books:
                
                book = Book(i[0],i[1],i[2])
                
                return str(book)

    #Adding book to the database
    def add_book(self,book):

        query = "INSERT INTO Library Values(?,?,?)"
        
        self.cursor.execute(query,(book.author,book.name,book.totalpages))
        self.connection.commit()

    #Deleting book from the database
    def delete_book(self,name):

        query = "DELETE FROM Library WHERE Name = ?"

        self.cursor.execute(query,(name,))
        self.connection.commit()

    #Searching for a book
    def search_book(self,name):
        
        query = "SELECT * FROM Library WHERE Name = ?"

        self.cursor.execute(query,(name,))

        book = self.cursor.fetchall()
        
        return book

    #This function sum the number of pages that you have read
    def sum_of_pages(self):
        query = "SELECT Total Pages FROM Library"

        self.cursor.execute(query)
        totalpages = self.cursor.fetchall()

        sum = 0

        if (len(totalpages) == 0):
            print("There aren't any book here")
        
        else:
            for i in totalpages:
                for j in i:
                    j = int(j)
                    sum = sum + j
        
        return sum
