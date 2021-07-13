# Identificate the prime numbers
number = int(input('Input of number: '))
defind_of_number = 'It is a prime number'
for each_number in range(2 ,number):
  if number % each_number == 0:
    defind_of_number = 'it is not a prime number'

print(defind_of_number)


# search in a range everything the prime numbers
range_of_number = 200
list_of_prime_numbers = []
for number in range(1, range_of_number+1):
  list_of_prime_numbers.append(number)
  for each_number in range(2, number):
    if number % each_number == 0:
      list_of_prime_numbers.remove(number)
      break

for see_data in list_of_prime_numbers:
  print(see_data)
