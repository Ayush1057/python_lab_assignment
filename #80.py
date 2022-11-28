#Ayush Sharma

def ci(principle, rate, time):

	
	Amount = principle * (pow((1 + rate / 100), time))
	CI = Amount - principle
	print("Compound interest is", CI)

ci(10000, 9.25, 3)
