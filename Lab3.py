def makebook(isbn,title,authors,qtystck,saleprice,genre,year):
    """constructor - creates a book"""
    return [isbn,title,authors,qtystck,saleprice,genre,year]

def bookshop():
    """constructor - creates a new bookshop"""
    return ("bookshop", [])

def add_book(book,bookshop):
    """constructor - adds a book to the bookshop"""
    return bookshop[1].append(book)


def books(bookshop):
    """accessor - returns the books of a bookshop"""
    return bookshop[1]

def get_Isbn(book):
    return book[0]

def get_Title(book):
    return book[1]

def get_Authors(book):
    return book[2]

#Get this checked out. It does correspond with the instructions.
def get_Qty(book):
    return book[3]

def get_Saleprice(book):
    return book[4]

def get_Genre(book):
    return book[5]

def get_Year(book):
    return book[6]

def coAuthors(book):
    if len(get_Authors(book)) == 1:
        return []
    elif len(get_Authors(book)) > 1:
        return get_Authors(book)[1:]

def check_price(isbn, bookshop):
    # Write your code here
    for i in range(len(books(bookshop))):
        if isbn == get_Isbn(books(bookshop)[i]):
            return get_Saleprice(books(bookshop)[i])
    return "Book not found"

def booksToReorder(reorder, bookshop):
    #print(bookshop)
    reorder_lst = []
    for i in range(len(books(bookshop))):
        if get_Qty(books(bookshop)[i]) <= reorder:
            #print(get_Isbn(books(bookshop)[i]))
            #print(get_Title(books(bookshop)[i]))
            reorder_lst += [(get_Isbn(books(bookshop)[i]), get_Title(books(bookshop)[i]))]
            #print(get_Qty(books(bookshop)[i]))
    #print("_",reorder_lst)
    return reorder_lst
            
                
        
