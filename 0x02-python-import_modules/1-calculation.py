#!/usr/bin/python3
from calculator_1 import add, subtract, multiply, divide
a = 10
b = 5

sum_result = add(a, b)
diff_result = subtract(a, b)
prod_result = multiply(a, b)
quotient_result = divide(a, b)

print("Sum of {} and {} = {}".format(a, b, sum_result))
print("Difference between {} and {} = {}".format(a, b, diff_result))
print("Product of {} and {} = {}".format(a, b, prod_result))
print("Quotient of {} divided by {} = {}".format(a, b, quotient_result))
