#!/usr/bin/python
# cpf validator (prints correct last two numbers)

import sys, re


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
	if digit < 2:
		return 0
	return 11 - digit


def computeDigit(cnpjNumbers, firstValidator = -1):
	sum = 0
	multiplier = 1

	if firstValidator != -1:
		cnpjNumbers += str(firstValidator)

	for i in range(0, len(cnpjNumbers)):
		multiplier += 1

		digit = int(cnpjNumbers[-(i+1)])
		sum += digit * multiplier

		if multiplier == 9:
			multiplier = 1

	return fixValidatorDigit(sum % 11)


def validate(cnpj):
	cnpjNumbers = re.sub(r'[^\d]', '', cnpj)

	if len(cnpjNumbers) != 14:
		print "Need 14 numbers"
		return False

	if isBlocked(cnpjNumbers):
		print "Invalid number"
		return False

	validNumbers = cnpjNumbers[:-2]
	firstValidator = computeDigit(validNumbers)
	secondValidator = computeDigit(validNumbers, firstValidator)

	if int(cnpjNumbers[-2]) == firstValidator and int(cnpjNumbers[-1]) == secondValidator:
		print "Number is right", cnpjNumbers
		return True

	print "Correct number: ", cnpjNumbers[:-2] + str(firstValidator) + str(secondValidator)
	return True

if len(sys.argv) > 0:
  numbers = iter(sys.argv)
  next(numbers)
  for number in numbers:
    # print number
    validate(number)
