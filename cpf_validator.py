#!/usr/bin/python
# cpf validator (prints correct last two numbers)

import sys, re
from random import randint


def isBlocked(n):
	def bySameNumber():
		for i in range(0, len(n)):
			if n[0] != n[i]:
				return False
		return True

	def byIncremental():
		for i in range(0, len(n)):
			if int(n[i]) != (i+1):
				return False
		return True
	
	return bySameNumber() or byIncremental()


def fixValidatorDigit(digit):
	if digit == 10:
		return 0
	return digit


def computeDigit(cpfNumbers, firstValidator = -1):
	initialValue = 10 if firstValidator == -1 else 11
	soma = 0
	for i in range(0, 9):
		soma += int(cpfNumbers[i]) * (initialValue-i)
	if firstValidator != -1:
		soma += firstValidator * 2
	return fixValidatorDigit(int(soma * 10 % 11))


def validate(cpf):
	cpfNumbers = re.sub(r'[^\d]', '', cpf)

	if len(cpfNumbers) < 9:
		print "Need at least 9 numbers"
		return False

	if isBlocked(cpfNumbers):
		print "Invalid number"
		return False

	firstValidator = computeDigit(cpfNumbers)
	secondValidator = computeDigit(cpfNumbers, firstValidator)

	if len(cpfNumbers) == 11 and int(cpfNumbers[9]) == firstValidator and int(cpfNumbers[10]) == secondValidator:
		print "Number is right:", cpfNumbers
		return True

	print "Correct number:", cpfNumbers[:9] + str(firstValidator) + str(secondValidator)
	return True


def generate():
	number = str(randint(100000000, 999999999))
	firstValidator = computeDigit(number)
	secondValidator = computeDigit(number, firstValidator)
	print "Valid number:", number + str(firstValidator) + str(secondValidator)


if len(sys.argv) > 1:
  numbers = iter(sys.argv)
  next(numbers)
  for number in numbers:
    # print number
    validate(number)
else:
	generate()

