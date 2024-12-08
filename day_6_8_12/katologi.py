import shutil
from pathlib import Path

base_path = Path('../ops_example')
base_path2 = Path('ops_example/D')

if base_path.exists() and base_path.is_dir():
    """Recursively delete a directory tree."""
    shutil.rmtree(base_path)  # usunięcie drzewa katalogów

base_path.mkdir()  # utworzenie katalogu

path_b = base_path / 'A' / 'B'
path_c = base_path / 'A' / 'C'
path_d = base_path / 'A' / 'D'

path_b.mkdir(parents=True)  # parents=True tworzy wszystkie potrzebne katalogi ze ścieżki, stworzy 'A'
path_c.mkdir()  # bo katalog 'A' juz istnieje

# utworzenie plików  wkatalogu path_b
for filename in ('ex1.txt', 'ex2.txt', 'ex3.txt'):
    with open(path_b / filename, "w", encoding='utf-8') as stream:
        stream.write(f'Jakaś treść w pliku {filename}')

# przenosi liki z katalogu B do katalogu D, usunie katalog B
shutil.move(path_b, path_d)  # przenieś
ex1 = path_d / 'ex1.txt'
# zmiana nazwy
ex1.rename(ex1.parent / 'ex1renamed.log')

print(base_path.absolute())  # scieżka na dysku bsolutna
# C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\day_6_8_12\..\ops_example
print(base_path.name)  # nazwa głównego katalogu
print(base_path.parent.absolute())
# C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\day_6_8_12\..
# r"C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\day_6_8_12\"
# C:\\Users\\Administrator\\PycharmProjects\\bootcamp16_11_2024\\day_6_8_12\\

print(base_path.suffix)
print(ex1.suffix)  # .txt
print(base_path.parts)
print(base_path2.parts)
# ('..', 'ops_example')
# ('ops_example', 'D')
