# tasks/task2.py

def solve():
# Ниже пишите решение задачи
x, y, z = map(int, input().split())
price_x = 3
price_y = price_x + 2
price_z = price_y + 7
print(price_x * x + price_y * y + price_z * z)

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()