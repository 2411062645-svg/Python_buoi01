# HOẠT ĐỘNG 6: ĐỆ QUY – GIAI THỪA, FIBONACCI

# Bài tập 6.1 - Giai thừa
def giai_thua_de_quy(n):
    if n <= 1:  # điều kiện dừng
        return 1
    return n * giai_thua_de_quy(n - 1)

def giai_thua_lap(n):
    ket_qua = 1
    for i in range(1, n + 1):
        ket_qua *= i
    return ket_qua

print("--- Hoạt động 6 ---")
print("Giai thừa de quy vs lap (5):", giai_thua_de_quy(5), "-", giai_thua_lap(5))

# Bài tập 6.2 - Số Fibonacci
def fibonacci_de_quy(n):
    if n <= 1:  # điều kiện dừng
        return n
    return fibonacci_de_quy(n - 1) + fibonacci_de_quy(n - 2)

print("Dãy Fibonacci (10 số đầu):")
for i in range(10):
    print(fibonacci_de_quy(i), end=" ")
print()