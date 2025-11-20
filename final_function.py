#MIT License

#Copyright (c) 2025 PAlv4r3z

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from addition import add
from substract import subtract
from multiply import multiply
from division import division

def calculator(operation, num1, num2):  #Evaluates operation and performs the specified operation with the numbers given
    if operation == 0:
        return add(num1, num2)
    if operation == 1:
        return subtract(num1, num2)
    if operation == 2:
        return multiply(num1, num2)
    if operation == 3:
        return divide(num1, num2)

operation = int(input("Type in 0 for +, 1 for -, 2 for * and 3 for /:" ))
num1 = int(input("Insert your first number: "))
num2 = int(input("Insert your first number: "))
print(calculator(operation, num1, num2))
