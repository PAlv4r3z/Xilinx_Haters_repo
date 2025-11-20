def subtract(num1, num2):
	# The following function subtracts two numbers, adding the first one the negative part of the second one
	if type(num1) != (int or float) or type(num2) != (int or float):
		return None
	num2 = -num2
	operation = num1 + num2
	return operation
