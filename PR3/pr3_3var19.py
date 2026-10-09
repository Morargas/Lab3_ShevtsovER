print("Введите размер сторон кирпича: a, b и c")
a = int(input())
b = int(input())
c = int(input())
print("введите стороны отверстия: r и s")
r = int(input())
s = int(input())
fits = False
if r <= s:
    holeMin = r
    holeMax = s
else:
    holeMin = s
    holeMax = r

if a <= b:
    min = a
    max = b
else:
    min = b
    max = a
if min <= holeMin and max <= holeMax:
    fits = True

if not fits:
    if a <= c:
        min = a
        max = c
    else:
        min = c
        max = a
    if min <= holeMin and max <= holeMax:
        fits = True

if not fits:
    if b <= c:
        min = b
        max = c
    else:
        min = c
        max = b
    if min <= holeMin and max <= holeMax:
        fits = True

if fits:
    print("Кирпич пройдет сквозь отверстие.")
else:
    print("Кирпич не пройдет сквозь отверстие.")