import unittest
import numpy
import gmpy2

def is_prime(nr):
	for i in range(2,nr):
		if (nr % i) == 0:
			return False
	return True
	
def is_armstrong(nr):
	strint = str(nr)
	l = len(strint)
	temp = nr
	sum = 0
	while temp > 0:
	   digit = temp % 10
	   sum += digit ** l
	   temp //= 10
	if nr == sum:
		return True	
	return False

def is_perfect(nr):
	sum = 0
	for i in range(1, nr):
		if(nr % i == 0):
			sum = sum + i
	if (sum == nr):
		return True
	return False
    

class Test_numbers(unittest.TestCase):
	def test_prime(self):
		p = 2
		for i in range(0,20):
			self.assertTrue(is_prime(p))
			p = gmpy2.next_prime(p)

	def test_armstrong(self):
		l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748]
		for armstrong_nr in l:
			self.assertTrue(is_armstrong(armstrong_nr))
		
		return
	
	def test_perfect(self):
		l = [6, 28, 496, 8128, 33550336]
		for perfect_nr in l:
			self.assertTrue(is_perfect(perfect_nr))
		return

unittest.main()



