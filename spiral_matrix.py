n = int(input('Введите число столбцов:'))
m = int(input('Введите число строк:'))
spiral = [[0]*n for _ in range(m)]
row, column, dr, dc = 0, 0, 0, 1

for i in range(1, n*m + 1):
    spiral[row][column] = i
    if row + dr >= m or row + dr < 0 or column + dc >= n or \
            column + dc < 0 or spiral[row + dr][column + dc]:
        dr, dc = dc, -dr
    row, column = row + dr, column + dc

for row in range(m):
    for column in range(n):
        print(str(spiral[row][column]).ljust(3), end='')
    print()

ex = input('Нажмите Enter для выхода')
