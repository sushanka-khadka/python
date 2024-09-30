print('prime check')

# is number prime
def only_prime_1(n):
  count = 0
  for i in range(1, n + 1):  # loop iniate n time
    if n % i == 0:
      count += 1
    else:
      pass
  print('Given number:',n, 'is',end=' ')
  if count == 0:
    print('neither prime nor composite')
  elif count == 2:
    print('prime')
  else:
    print('composite')


only_prime_1(-5)  # neither prime nor composite
only_prime_1(0) # neither prime nor composite
only_prime_1(2) # prime
only_prime_1(1) # composite


# prime check for list of numbers
def only_prime(li):
  prime.clear()   # clears the set every time function is called
  for item in li:
    count = 0
    for i in range(1, item + 1):  # loop initiated n time
      if item % i == 0:
        count += 1
    if count == 2:
      prime.add(item)
    else:
      pass


prime = set()

print('\n\n list of prime numbers')
list_1 = list(range(-50,100))
only_prime(list_1)
prime_list= list(prime)
prime_list.sort()
print(prime_list)
