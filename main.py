result = []

def divider(a, b):
    if a < b:
        raise ValueError("a должно быть больше или равно b")
    if b > 100:
        raise IndexError("b не должно быть больше 100")
    if b == 0:
        raise ZeroDivisionError("На ноль делить нельзя")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Ошибка при обработке {key}: {e}")

print(result)