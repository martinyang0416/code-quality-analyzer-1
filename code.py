a = int(input())
fact = 1
for i in range(1, a + 1):
    fact *= i
binary_representation = bin(fact)[2:]  # Remove the '0b' prefix
print(binary_representation.count('1'))