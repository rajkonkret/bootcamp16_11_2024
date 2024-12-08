import main
import pakiet  # import calego pakietu, sterowany przez __all__
from pakiet import fun  # import konkretnego pliku z pakietu
import pakiet.fun as pk  # jako alias

main.print_hi("Radek")  # Hi, Radek

# pakiet.powitanie()  # AttributeError: module 'pakiet' has no attribute 'powitanie'

# from pakiet import fun
fun.powitanie()
fun.info()

# import pakiet.fun as pk # jako alias
pk.powitanie()
pk.info()
# Hi, Radek
# Cześć
# Jestem pakietem
# Cześć
# Jestem pakietem

# # strowanie widocznością elelemntów pakietu
# __all__ = ['info']
pakiet.info()  # Jestem pakietem
