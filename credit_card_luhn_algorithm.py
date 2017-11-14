#!/usr/bin/python
# luhn (credit card validation)

import sys, re
from random import randint

def brand_definitions():
  irange = lambda start, end: range(start, end+1)
  irange_s = lambda start, end: map(str, irange(start, end))
  
  return [
    {'brand': 'visa',           'len': [13, 16, 19],    'prefix': ['4']},
    {'brand': 'mastercard',     'len': [16],            'prefix': irange_s(51, 55)},
    {'brand': 'amex',           'len': [15],            'prefix': ['34', '37']},
    {'brand': 'diners club',    'len': irange(14, 19),  'prefix': ['36']},
    {'brand': 'diners club',    'len': irange(16, 19),  'prefix': irange_s(300, 305) + ['3095'] + irange_s(38, 39)},
    {'brand': 'discover card',  'len': irange(16, 19),  'prefix': ['6011', '64', '65']},
    {'brand': 'maestro',        'len': irange(12, 19),  'prefix': ['50'] + irange_s(56, 58) + ['6']},
    {'brand': 'mastercard',     'len': [16],            'prefix': irange_s(22210, 22720)},
  ]


def check_brand_and_length(number):
  probably = []
  def save_as_possible(b):
    if b not in probably:
      probably.append(b)

  def has_valid_length(b):
    if len(number) in b['len']:
      print "Brand: ", b['brand']
      return True
    else:
      return False

  found = False
  brands = brand_definitions()
  for b in brands:
    for p in b['prefix']:
      if number.startswith(p):
        save_as_possible(b)
        found = has_valid_length(b)
      if found: break
    if found: break
  if not found:
    if len(probably) > 0:
      print 'please check number length. Card is probably for one of these brands:\n', map(lambda x: x['brand'], probably)
    else:
      print 'unknow brand'
    return False
  else:
    return True


def luhn(number):
  digits = map(int, list(number))
  digits.reverse()

  sum = 0
  for index, digit in enumerate(digits):
    if index % 2 == 0:
      sum += digit
    else:
      digitTwice = digit * 2
      digitTwiceFixed = digitTwice / 10 + digitTwice % 10
      sum += digitTwiceFixed
      
  if sum % 10 != 0:
    correctCheckDigit = 10 - (sum - digits[0]) % 10
    return correctCheckDigit
  else:
    return -1


def generate(prefix, length):
  brands = brand_definitions()
  ok = False
  for b in brands:
    for p in b['prefix']:
      if p.startswith(prefix) or prefix.startswith(p):
        if length not in b['len']:
          print 'Invalid length'
        else:
          ok = True
        break
    if ok:
      break
  if ok:
    missing_length = length - len(prefix)
    number = int(prefix)
    for i in range(0, missing_length):
      number = number*10 + randint(0, 10)
    validator_digit = luhn(str(number))
    if validator_digit != -1:
      number = number / 10 * 10 + validator_digit
    print number
  else:
    print "Invalid prefix"




if len(sys.argv) > 1:
  numbers = iter(sys.argv)
  next(numbers)
  for number in numbers:
    if number == 'create':
      prefix = next(numbers)
      length = int(next(numbers))
      generate(prefix, length)

    else:
      valid_brand = check_brand_and_length(number)

      if valid_brand:
        verification_number = luhn(number)
        fixed_number = number[:-1] + str(verification_number)
        if verification_number != -1:
          print 'fixed number', fixed_number
        else:
          print 'number is valid'



else:
  msg = """Card numbers (https://en.wikipedia.org/wiki/Payment_card_number):
Brand         | Length         | Prefix
--------------|----------------|------------
visa          | 13, 16, 19     | 4
mastercard    | 16             | 51..55
amex          | 15             | 34, 37
diners club   | 14..19         | 36
diners club   | 16..19         | 300..305, 3095, 38..39
discover card | 16..19         | 6011, 64, 65
maestro       | 12..19         | 50, 56..58, 6
mastercard    | 16             | 2221..2720
"""
  print msg