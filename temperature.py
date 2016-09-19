import argparse

def K2C(K):
	return round((K-273.15),3)

def C2K(C):
	return round((C+273.15),3)

def F2C(F):
	return round(((F-32)*5/9),3)

def C2F(C):
	return round((C*9/5+32),3)

def F2K(F):
	return round(C2K(F2C(F)),3)

def K2F(K):
	return round(C2F(K2C(K)),3)

