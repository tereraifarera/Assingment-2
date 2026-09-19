import random

numbers = [random.uniform(0, 10) for _ in range(5)]

print("Generated numbers:", [round(n, 2) for n in numbers])
print(f"Minimum: {min(numbers):.2f}")
print(f"Maximum: {max(numbers):.2f}")