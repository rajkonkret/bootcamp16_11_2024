import numpy_rozpoznawanie_cyfr as nrc

import os
from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt
from typing import List


def load_all_images_from_directory(directory_path: str, size: int = 28, invert: bool = False) -> List[np.ndarray]:
    """
    Wczytuje wszystkie obrazy PNG z podanego katalogu, skaluje do rozmiaru 28x28 i konwertuje do tablic NumPy.

    :param directory_path: Ścieżka do katalogu z obrazami PNG.
    :param size: Docelowy rozmiar obrazów (domyślnie 28x28).
    :param invert: Czy odwracać kolory obrazu (czarne na białe i odwrotnie).
    :return: Lista tablic NumPy z obrazami o wymiarach (28, 28).
    """
    image_arrays = []
    image_data = []


    # Przechodzimy przez wszystkie pliki w katalogu
    for file_name in os.listdir(directory_path):
        if file_name.lower().endswith('.png'):
            file_path = os.path.join(directory_path, file_name)
            try:
                # Wczytanie obrazu i konwersja do odcieni szarości
                image = Image.open(file_path).convert('L')

                # Opcjonalne odwrócenie kolorów
                if invert:
                    image = ImageOps.invert(image)

                # Zmiana rozmiaru obrazu
                image = image.resize((size, size))

                # Konwersja obrazu do tablicy NumPy i normalizacja
                image_array = np.array(image).astype(np.float32) / 255.0

                # image_arrays.append(image_array)
                image_data.append((image_array, file_name))
            except Exception as e:
                print(f"Nie udało się przetworzyć pliku: {file_name}. Błąd: {e}")


    return image_data


if __name__ == '__main__':
    # Ścieżka do katalogu z obrazami PNG
    directory_path = './'

    # Wczytanie wszystkich obrazów PNG z katalogu z odwróceniem kolorów
    images = load_all_images_from_directory(directory_path, invert=True)

    print(f"Wczytano {len(images)} obrazów.")

    # Wyświetlenie pierwszego obrazu
    for image, label in images:
        plt.imshow(image, cmap='gray')
        plt.axis('off')
        plt.title('Pierwszy obraz z katalogu')
        plt.show()
        result =  nrc.predict_image(image)

        print(f"Label: {label}")
        print(f"PREDICTED DIGIT: {result[0]}")
