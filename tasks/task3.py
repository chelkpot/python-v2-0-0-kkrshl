# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    a, b, = map(int, input().split())
total = a + b - 1
garry_remaining = total * a
larry_remaining = total - b
print(garry_remaining, larry_remaining)


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()