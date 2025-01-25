from decimal import Decimal


def calculate_gross_price(net_price, vat):
    net_price = Decimal(net_price)
    vat_rate = Decimal(vat) / 100
    gross_price = net_price + (net_price * vat_rate)
    return gross_price.quantize(Decimal("0.01"))


price_netto = "100.99"
vat = 23
price_brutto = calculate_gross_price(price_netto, vat)

print(f"""
cena netto: {price_netto}
Vat: {vat}
cena brutto: {price_brutto}
""")
# cena netto: 100.99
# Vat: 23
# cena brutto: 124.22
