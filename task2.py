import math


def series_function(k, x):
    return ((-1) ** k * k / (k ** 2 - 1)) * math.sin(k * x)


def compute_series(a, b, h, d):
    x_values = []
    y_values = []

    x = a



    while x <= b:
        result = 0
        k = 2
        while True:


            term = series_function(k, x)
            result += term

            if abs(term) <= d:
                print("Fault")
                break


            k += 1

        x_values.append(x)
        y_values.append(result)

        x += h

    return x_values, y_values


# Вказати інтервал, крок табуляції та похибку
a = -1
b = 1
h = 0.2
d = 0.001

x_values, y_values = compute_series(a, b, h, d)

# Вивести результати табуляції
print("x\t\tf(x)")
for x, y in zip(x_values, y_values):
    print(f"{x:.2f}\t\t{y:.4f}")
