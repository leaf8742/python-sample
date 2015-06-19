#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fib(max):
	a, b = 0, 1
	for n in range(max):
		yield b
		a, b = b, a + b
	return 'done'

def yieldfrom(max):
	print('0')
	yield from fib(max)
	print('1')
	print('2')


print(list(yieldfrom(10)))

