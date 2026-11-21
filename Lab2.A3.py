import string 

print("Ввод: ")

Gas = int(input())

LastGas = int(input())

RealGas = 0

Pay = float(0)

print("Предыдущее")

print(Gas)

print("Текущее")

print(LastGas)

print("Использовано")

if LastGas >= Gas:
    RealGas = LastGas - Gas
else:
    RealGas = 10000 - Gas + LastGas

print(RealGas)

if RealGas <= 300:
    Pay = 21
    print("К оплате")
    print(f"{Pay:.2f}")

if RealGas > 300 and RealGas <= 600:
    RealGas = RealGas - 300
    Pay = 21 + RealGas * 0.06
    print("К оплате")
    print(f"{Pay:.2f}")

if RealGas > 600 and RealGas <= 800:
    Pay = 21 + (300 * 0.06) + (RealGas - 600) * 0.04
    print("К оплате")
    print(f"{Pay:.2f}")

if RealGas > 800:
    Pay = 21 + 300 * 0.06 + 200 * 0.04 + (RealGas - 800)* 0.025
    print("К оплате")
    print(f"{Pay:.2f}")

if RealGas > 0:
    cr = Pay / RealGas
    print("Ср. цена m^3 ")
    print(f"{cr:.3f}")
else:
    print("0")