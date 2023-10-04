# Gerador de Senhas Seguras

import random

uppercase_letter = chr(random.randint(65, 90))
lowercase_letter = chr(random.randint(97, 122))
special_char = chr(33)
numbers_list = []

for i in range(5): #até 8 dígitos
  numbers = random.randrange(9)
  numbers_list.append(numbers)
random.shuffle(numbers_list)
numbers_list = str(numbers_list) [1:-1]
numbers_list = numbers_list.replace(',', '')

print(uppercase_letter, lowercase_letter, numbers_list, special_char)