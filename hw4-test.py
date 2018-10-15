#!/usr/bin/python3
# student test file for HW4

import unittest
from hw4 import *
#====================================
TIMEOUT_SHORT = 1
TIMEOUT_LONG = 10

class tester_most_common_char(unittest.TestCase):
	# O(k) time and space
	def test__given(self):
		self.assertEqual(most_common_char('AVX is a feature in modern CPUs that allows one instruction to affect multiple units. vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvectors'), 'v')
		self.assertIn(most_common_char('aabbaabb'), ['a','b'])

class tester_alphabet_finder(unittest.TestCase):
	# O(k) time and space
	def test__given(self):
		test = 'qwertyuiopASDFGHJKLzxcvbnm insensitive paella'
		result = test[:26]
		self.assertEqual(alphabet_finder(test), result)
		test = 'aardvarks are cool!'
		result = None
		self.assertEqual(alphabet_finder(test), result)

# class tester_longest_unique_subarray(unittest.TestCase):
# 	# O(k) time and space
# 	def test__given(self):
# 		self.assertEqual(tuple(longest_unique_subarray([1, 2, 3, 1, 4, 5, 6])), (1, 6))
# 		self.assertEqual(tuple(longest_unique_subarray(list(range(10)))), (0, 10))

class tester_string_my_one_true_love(unittest.TestCase):
	# O(k) time and space
	def test__given(self):
		self.assertTrue(string_my_one_true_love('abcbabcdcdda'))
		self.assertTrue(string_my_one_true_love('aaabbbcccddde'))
		self.assertFalse(string_my_one_true_love('aaabbbcccdddeeffgg'))

# class tester_alive_people(unittest.TestCase):
# 	# O(k log k) time, O(k) space
# 	# under certain circumstances O(k) solution MIGHT exist?@timeout_decorator.timeout(TIMEOUT_SHORT)
# 	def test__given(self):
# 		self.assertEqual(alive_people([[1920, 80], [1940, 22], [1961, 10]]), 1961)

# class tester_three_sum(unittest.TestCase):
# 	# O(k^2) time and space
# 	def _transform(self, result):
# 		result = list(result)
# 		for i in range(len(result)):
# 			result[i] = sorted(list(result[i]))
# 		result.sort()
# 		return result
	#
	# def test__given(self):
	# 	result = three_sum([-1, 0, 1, 2, -1, -4], 0)
	# 	ex = [[-1, 0, 1], [-1, -1, 2]]
	# 	result = self._transform(result)
	# 	ex = self._transform(ex)
	# 	self.assertEqual(result, ex)

# class tester_happy_numbers(unittest.TestCase):
# 	# O(k log k) time, O(log k) space
# 	def test__given(self):
# 		self.assertEqual(happy_numbers(8), 2468 // 1234)
# 		self.assertEqual(happy_numbers(15), 4)
#
# # class tester_zero_sum_subarray(unittest.TestCase):
# 	# O(k) time and space
# 	def test__given(self):
# 		self.assertEqual(tuple(zero_sum_subarray([0, 1, 2, 3, 4, 5])), (0, 1))
# 		self.assertEqual(tuple(zero_sum_subarray([10, 20, -20, 3, 21, 2, -6])), (1, 2))
#===================================
# BOILERPLATE CODE

# suppress stdout, but keep stderr since that's what unittest use
# https://stackoverflow.com/questions/30715337
from io import StringIO
import sys

class ReplaceStd(object):
	""" Let's make it pythonic. """
	def __init__(self):
		self.stdout = None

	def __enter__(self):
		self.stdout = sys.stdout
		sys.stdout = StringIO()

	def __exit__(self, type, value, traceback):
		sys.stdout.close()
		sys.stdout = self.stdout

if __name__ == "__main__":
	with ReplaceStd():
		unittest.main(module=__name__, buffer=True, exit=False)
