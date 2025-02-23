# Symuluj 1000 scenariuszy inwestycyjnych dla portfela o początkowej wartości 10000 PLN,
# przy średnim rocznym zwrocie 7% i odchyleniu standardowym 15%.
# 	•	Oblicz wartość portfela po 10 latach dla każdego scenariusza.
# 	•	Znajdź najlepszy, średni i najgorszy scenariusz.

import numpy as np

initial_value = 10000
years = 10
annual_return = 0.07
annual_volatility = 0.15
simulations = 1000

np.random.seed(42)

annual_growth_rates = np.random.normal(annual_return, annual_volatility, (years, simulations))
values = initial_value * np.cumprod(1 + annual_growth_rates, axis=0)

print(values)
final_values = values[-1]
print("Srednia wartość portfela po 10 latach:", np.mean(final_values))
print("Najlepszy scenariusz:", np.max(final_values))
print("Najgorszy scenariusz:", np.min(final_values))
# Srednia wartość portfela po 10 latach: 19619.038188903683
# Najlepszy scenariusz: 70912.47810765122
# NAjgorszy scenariusz: 3710.4127579491196
