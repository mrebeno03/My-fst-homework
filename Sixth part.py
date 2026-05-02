import sys
print("Введіть кількість балів з екзамену: ")
a = int(input())
if a <= 49:
    print("Незадовільно.")
    sys.exit()
if a <= 69:
    print("Задовільно.")
    sys.exit()
if a <= 89:
    print("Добре.")
    sys.exit()
if a <= 100:
    print("Відмінно.")
    sys.exit()
if a > 100:
    print("Агов! Зоставайся на землі приятелю!")