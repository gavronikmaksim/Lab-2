import sys 

print("Введите координаты x1 и x2:")
x1 = int(input())
x2 = int(input())

print("Введите координаты y1 и y2:")
y1 = int(input())
y2 = int(input())

if ( x1 == 0 or y1 == 0 or x2 == 0 or y2 == 0 ) :
    print("В координатах не должно быть нулей")

if (x1 > 0 and y1 > 0 and x2 > 0 and y2 > 0) :
    print("Входит, 1ая четверть")

if (x1 < 0 and y1 > 0 and x2 < 0 and y2 > 0) :
    print("Входит, 2ая четверть")

if (x1 < 0 and y1 < 0 and x2 < 0 and y2 < 0) :
    print("Входит, 3ая четверть")

if (x1 > 0 and y1 < 0 and x2 > 0 and y2 < 0) :
    print("Входит, 4ая четверть")
else :
    print("Никуда не входит")
