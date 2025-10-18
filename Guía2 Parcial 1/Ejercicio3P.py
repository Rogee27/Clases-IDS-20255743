"""X = int(input())
A = input()
B = input()

print(A[:X:]+B[-X:])"""

X = int(input())
A = input()
B = input()

p1 = int(len(A)/X)
p2 = int(len(B)/X)

print(f"{A[:p1]}{B[-p2:]}")



