import unittest
import sys
import leapYear
#solution to check stdout found from https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python/17981937
class TestCase(unittest.TestCase):
	def test1(self):
		#calls print function of program
		leapYear.leap(2020)
		#check if using buffer
		if not hasattr(sys.stdout,"getvalue"):
			self.fail("need to run in buffered mode")
		#save stdout as ouput
		output = sys.stdout.getvalue().strip()
		#compares stdout with that it's supposed to be
		self.assertEqual(output,'2020 is a leap year!')
	def test2(self):
		#calls print function of program
		leapYear.leap(2017)
		#check if using buffer
		if not hasattr(sys.stdout,"getvalue"):
			self.fail("need to run in buffered mode")
		#save stdout as ouput
		output = sys.stdout.getvalue().strip()
		#compares stdout with that it's supposed to be
		self.assertEqual(output,'2017 is not a leap year!')
	def test3(self):
		#calls print function of program
		leapYear.leap(1500)
		#check if using buffer
		if not hasattr(sys.stdout,"getvalue"):
			self.fail("need to run in buffered mode")
		#save stdout as ouput
		output = sys.stdout.getvalue().strip()
		#compares stdout with that it's supposed to be
		self.assertEqual(output,'1500 is not a leap year!')
	def test4(self):
		#calls print function of program
		leapYear.leap(2000)
		#check if using buffer
		if not hasattr(sys.stdout,"getvalue"):
			self.fail("need to run in buffered mode")
		#save stdout as ouput
		output = sys.stdout.getvalue().strip()
		#compares stdout with that it's supposed to be
		self.assertEqual(output,'2000 is a leap year!')
if __name__ == '__main__':
	assert not hasattr(sys.stdout,"getvalue")
	unittest.main(module=__name__, buffer = True,exit=False)



