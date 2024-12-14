from pprint import pprint


class PrintMedia:
    def print_media(self):
        print("Drukowana treść")


class DigitalMedia:
    def digital_media(self):
        print("Cyfrowa treść")


class Book(PrintMedia):
    pass


class Ebook(DigitalMedia):
    pass


class MultimediaBook(Book, Ebook):
    pass


multimedia_book = MultimediaBook()
pprint(MultimediaBook.__mro__)
# (<class '__main__.MultimediaBook'>,
#  <class '__main__.Book'>,
#  <class '__main__.PrintMedia'>,
#  <class '__main__.Ebook'>,
#  <class '__main__.DigitalMedia'>,
#  <class 'object'>)

multimedia_book.print_media()
multimedia_book.digital_media()
# Drukowana treść
# Cyfrowa treść
