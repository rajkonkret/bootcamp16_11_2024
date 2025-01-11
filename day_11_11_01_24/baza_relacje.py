# relacje w bazach danych
# typy relacji

# jeden do jednego - Obydwie tabele mogą zawierać tylko jeden rekord po każdej stronie
# Każda wartość klucza podstawowego dotyczy tylko jednego lub nie dotyczy żadnego rekordu w tabeli powiązanej.
# Relacje "jeden do jednego" są w większości wymuszane przez reguły biznesowe i nie wynikają w sposób naturalny z danych.
# Jeśli taka reguła nie obowiązuje, możliwe jest łączenie obydwu tabel bez naruszania reguł normalizacji.

# jeden do wielu - tabele klucza podstawowego zawiera tylko jeden rekord, dotyczy jedenego, żadnego,
# wielu rekordów w powiązanej tabeli

# wiele do wiele - kazdy rekord obydwu tabel mozę odnośić się do dowolnej liczby rekordów
# W przypadku takich relacji wymagana jest trzecia tabela nazywana tabelą powiązań,
# ponieważ systemy relacyjne nie mogą bezpośrednio obsługiwać takiej relacji.
