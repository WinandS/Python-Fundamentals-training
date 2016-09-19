import unittest
import temperature as t

class Test_numbers(unittest.TestCase):
	def test_K2C(self):
		self.assertAlmostEqual(t.K2C(300), 26.85)

	def test_C2K(self):
		self.assertAlmostEqual(t.C2K(26.85), 300)

	def test_F2C(self):
		self.assertAlmostEqual(t.F2C(212), 100)

	def test_C2F(self):
		self.assertAlmostEqual(t.C2F(100), 212)

	def test_F2K(self):
		self.assertAlmostEqual(t.F2K(212), 373.15)

	def test_K2F(self):
		self.assertAlmostEqual(t.K2F(373.15), 212)
		

unittest.main()
