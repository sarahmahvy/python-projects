def is_power_of_two(number):
  if number == 0:
    return False
  while number % 2 == 0:
    number = number / 2
  if number == 1:
    return True
  return False
  
response = True
while response:
  number = int(input("Enter a number to check if it is a power of two: "))
  print(is_power_of_two(number))
  response = input("Do you want to continue? (y/n): ")
  if response.lower() == 'n':
    response = False