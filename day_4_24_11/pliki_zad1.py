# praca z plikami
# t = open("nazwa_pliku","parametr")
# context manager
# with
# to pozwala na bezpieczniejszą pracę z plikami
#  ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open("test.log", "w", encoding='utf-8') as fh:  # filehandler
    fh.write("Powitanie\n")
    fh.write("Kolejne\n")
    fh.write("Jeszcze jedno\n")

with open("../test.log", "w", encoding='utf-8') as fh:  # filehandler, ten plik bedzie w nadrzędnym katalogu
    fh.write("Powitanie\n")

# w - kasuje plik jesli istnieje
with open("../test.log", "w") as fh:  # filehandler, ten plik bedzie w nadrzędnym katalogu
    fh.write("Nadpisane\n")

# x bład jesli plik juz istnieje
# FileExistsError: [Errno 17] File exists: '../test.log'
# with open("../test.log", "x", encoding='utf-8') as fh:  # filehandler, ten plik bedzie w nadrzędnym katalogu
#     fh.write("Powitanie\n")
# gdy plik nieistnieje zostanie utworzony
# with open("../test_2.log", "x", encoding='utf-8') as fh:  # filehandler, ten plik bedzie w nadrzędnym katalogu
#     fh.write("Nadpisane\n")

with open("test.log", "a", encoding='utf-8') as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dośdane\n")

with open("test.log", "r", encoding='utf-8') as f:
    lines = f.read()

# encoding='utf-8' - ustawienie kodowania na utf-8
print(lines)
# Powitanie
# Kolejne
# Jeszcze jedno
# Dodane
# Dodane
# Dodane
# Dodane
# Dośdane
