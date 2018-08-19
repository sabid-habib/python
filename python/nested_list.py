
n = int(input())

std = [[input(), float(input())] for i in range(n)]

second= sorted(list(set([mark for name,mark in std])))[1]

print('\n'.join([a for a,b in sorted(std) if b==second]))
