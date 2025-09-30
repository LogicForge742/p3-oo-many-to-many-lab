class Book:
    def __init__(self, title:str):
        if not isinstance(title , str):
            raise TypeError("Title must be a string")
        self.title = title

    def contracts(self):

        return[contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return[contract.author for contract in Contract.all if contract.book == self]




class Author:
    def __init__(self, name:str):
        if not isinstance(name ,str):
            return TypeError("Name must be a string")
        self.name = name
    def contracts(self ):
        return [contract for contract in Contract.all if contract.author == self]
    
   
    def books(self):
        #return 
          return[contract.book for contract in Contract.all if contract.author == self]
    

    def sign_contract( self ,book, date, royalties):
        contract = Contract(self,book,date,royalties )
        return contract
    
    def total_royalties(self):

        return  sum([contract.royalties for contract in Contract.all if contract.author == self])


class Contract:
    all = []
    def __init__(self, author:Author, book:Book,date:str ,royalties:int):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("Royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

        
    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in Contract.all if contract.date == date]
      
