import chardet

# pip install chardet
with open("test.log", "r") as file:
    lines = file.read()

print(lines)
# Powitanie
# Kolejne
# Jeszcze jedno
# Dodane
# Dodane
# Dodane
# Dodane
# DoĹ›dane
with open("test.log", "r", encoding='utf-8') as file:
    lines = file.read()

print(lines)
# Powitanie
# Kolejne
# Jeszcze jedno
# Dodane
# Dodane
# Dodane
# Dodane
# Dośdane

file_path = "test.log"
with open(file_path, 'rb') as file:  # rb - odczyt bajtowy
    raw_data = file.read()

print(raw_data)
# b'Powitanie\r\nKolejne\r\nJeszcze jedno\r\nDodane\r\nDodane\r\nDodane\r\nDodane\r\nDo\xc5\x9bdane\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'MacRoman', 'confidence': 0.6460919540229885, 'language': ''}
# Po zwiększeniu próbki czyli więcej polskich znaków w teksie wynik poprawny
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']
confidence = result['confidence']
print("Kodowanie znaków:", encoding)
print("Trafność:", confidence)

print(raw_data.decode(encoding=encoding))
# Kodowanie znaków: utf-8
# Trafność: 0.99
# Powitanie
# Kolejne
# Jeszcze jedno
# Dodane
# Dodane
# Dodane
# Dodane
# Dośdane
# Dośźąćńdane
