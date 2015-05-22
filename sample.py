#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

g_primes = {"max":1, "primes":[]}

def fn_primes(x):
	if x < 2:
		return []
	elif x == 2:
		return [2, ]

	v_primes = fn_primes(x - 1)
	condition = False
	position = int(math.sqrt(x)) + 1

	for prime in v_primes:
		if prime > position:
			break
		elif x % prime == 0:
			condition = True
			break

	if not condition:
		v_primes.append(x)

	return v_primes

def fn_not_prime(x):
	if x in fn_primes(x):
		return False
	else:
		return True

###
 # @function fn_sigma(∑)
 # @brief 等差数列求和公式
 # @see http://baike.baidu.com/link?url=m9jRLvZLJdl9_41rx0_0VMzshMRLjiH0B-SANBATlvoaJYLYRUJMLS-paa5lg73iiT999RgV0D72IeEULUSMkK
 # @param begin 第一个数
 # @param end 最后一个数
 # @param count 数列个数
 # @param step 公差
##
def fn_sigma(begin, end, count, step):
	# 求和公式1，适合步进为1的数列
#	return (begin + end) * count / 2
	# 求和公式2
#	return count * begin + count * (count - 1) / 2 * step
	# 求和公式3
	return (2 * begin + (count - 1) * step) * count / 2
	# 求和公式4
#	return (d / 2.) * pow(n, 2) + (a1 - d / 2.) * n

#print primes(1000)
print filter(fn_not_prime, range(1, 100))

