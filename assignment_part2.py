class Book:
    author = ""
    title = ""
    def __init__(self, author, title):
        self.author = author
        self.title = title
    def display(self):
        print("{}, written by {}".format(self.title, self.author))

OMM = Book('John Steinbeck','Of Mice and Men')
TKM = Book('Harper Lee','To Kill a Mocking Bird')

OMM.display()
TKM.display()