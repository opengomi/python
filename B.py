# coding=utf-8

def f(n):
	a = 1;
	for i in range(1, n + 1):
		a = a * i
	return a

value = int(raw_input('값!: '))
print f(value)
