class book():
    def __init__(self,name,year,price,author):
        self.book_name  = name
        self.book_year = year
        self.book_price = price
        self.book_author = author
    
    def add_citizen(self):
        print("name: "+self.book_name)
        print("year of publish: "+str(self.book_year))
        print("age: "+self.book_price)
        print("author: "+self.book_author)

book1 = book("Harry Potter",1997,"1998","J.K Rowling")
book1.add_citizen()

book2 = book("Diary of wimp kid",2017,"700","Jeff Kinney")
book2.add_citizen()
    