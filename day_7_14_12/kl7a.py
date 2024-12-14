from pprint import pprint


class Printer:
    def print_message(self, message):
        print(f"Drukowanie wiadomości {message}")


class Scanner:
    def scan_document(self):
        print("Skanowanie dokumentu")
        return "Zawartość dokumentu"


printer = Printer()
printer.print_message("Radek")  # Drukowanie wiadomości Radek

scanner = Scanner()
print(scanner.scan_document())


# Skanowanie dokumentu
# Zawartość dokumentu

# klasa Mixin
class MultifunctionDevice(Printer, Scanner):

    def photocopy(self):
        content = self.scan_document()
        self.print_message(content)


device = MultifunctionDevice()
device.photocopy()
# Skanowanie dokumentu
# Drukowanie wiadomości Zawartość dokumentu

message = device.scan_document()
print(message)
# Skanowanie dokumentu
# Zawartość dokumentu

device.print_message(message)
# Drukowanie wiadomości Zawartość dokumentu

pprint(MultifunctionDevice.__mro__)
# (<class '__main__.MultifunctionDevice'>,
#  <class '__main__.Printer'>,
#  <class '__main__.Scanner'>,
#  <class 'object'>)
