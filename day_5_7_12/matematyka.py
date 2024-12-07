import math

x = min(5, 10, 20)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)
# 7.25
print(x)

x = pow(4, 3)  # 64
print(x)
print(4 ** 3)  # 64

print(math.pi)  # 3.141592653589793

x = math.sqrt(64)
print(x)  # 8.0

x = math.ceil(1.4)
print(x)  # 2, zaokrągla w góre
y = math.floor(1.4)
print(y)  # 1, zaokragla w dół

x = math.cos(90)
print(x)
radian = math.radians(180)
print(radian)  # 3.141592653589793
x = math.cos(radian)
print(x)  # -1.0

x = math.exp(2)
print(f"e ^ 2 = {x}")  # e ^ 2 = 7.38905609893065

log_val = math.log(10)
print(f"Log: {log_val}")  # Log: 2.302585092994046

log10_val = math.log10(10)
print(f"Log10: {log10_val}")  # Log10: 1.0
