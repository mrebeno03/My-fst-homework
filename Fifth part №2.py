##Складний варіант без використання звичайної функції з math##
print("Введи число")
a = int(input())
result = 1
for i in range(a, 0 , -1):
    result = result * i
print(result)