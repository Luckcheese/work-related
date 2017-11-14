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


#  12.740.852/0001-02
#  numbers: 127408520001      digitos: 02



#      var numeros, digitos, soma, i, resultado, pos, tamanho, digitosIguais;
#      if (!digitosIguais) {
#        tamanho = cnpj.length - 2;
#        numeros = cnpj.substring(0, tamanho);
#        digitos = cnpj.substring(tamanho);
#        soma = 0;
#        pos = tamanho - 7;
#        for (i = tamanho; i >= 1; i--) {
#          soma += numeros.charAt(tamanho - i) * pos--;
#          if (pos < 2) {
#            pos = 9;
#          }
#        }
#        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
#        if (resultado.toString() !== digitos.charAt(0)) {
#          return false;
#        }
#        tamanho = tamanho + 1;
#        numeros = cnpj.substring(0, tamanho);
#        soma = 0;
#        pos = tamanho - 7;
#        for (i = tamanho; i >= 1; i--) {
#          soma += numeros.charAt(tamanho - i) * pos--;
#          if (pos < 2) {
#            pos = 9;
#          }
#        }
#        resultado = soma % 11 < 2 ? 0 : 11 - soma % 11;
#        if (resultado.toString() !== digitos.charAt(1)) {
#          return false;
#        }
#        return true;
#      }
#      else {
#        return false;
#      }
