import unittest
import numpy as np

def dict_inverse(dic):
	new_keys=[]
	dic_inv={}
	for key, value in dic.items():
		if value not in new_keys:
			new_keys.append(value)
			dic_inv.update({value : key})
		else:
			list_keys = dic_inv[value]
			list_keys = np.hstack((list_keys, key))
			dic_inv.update({value : list_keys})
	return dic_inv


class Test_dict_inverse(unittest.TestCase):
	def test_dict_inverse(self):
		d = { "Oostende" : 8400, 
			"Zandevoorde" : 8400,
			"Stene" : 8400,
			"Brugge" : 8000,
			"Gent" : 9000
			}
		d2 = dict_inverse(d)
		
		for item in d2.items():
			print item[0], item[1]	
		
		self.assertEqual(len(d2), 3)
		self.assertEqual(len(d2[8400]), 3)
		for city in ("Oostende","Zandevoorde","Stene"):
			self.assertTrue(city in d2[8400])

		self.assertEqual(d2[8000], "Brugge")
		self.assertEqual(d2[9000], "Gent")

unittest.main()
