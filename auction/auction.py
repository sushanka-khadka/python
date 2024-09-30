#  program to bid for messi's jersey

# def new_bid(name,price):
#   auction.update({name:price})
  
auction ={}
auction.update({'lowest':150})
bid='yes'
while (bid == 'yes'):
  name = input('what is your name: ')
  price = float(input('what is your bid(in k)? रु'))
  
  max_bid = max(list(auction.values()))
  if price > max_bid:
    # new_bid(name,price)
    # auction.update({name:price})
    auction[name]=price
  else:
    print(f'not enough for bid!\n highest bid is {max_bid}')

  bid = input('do you want to bid again? yes or no: ').lower()


for key,value in auction.items():
  if value == max(list(auction.values())):
    name = key
    price = value

print(f'\nJesey sold to {name} for {price}k' )

print(auction)
# print(list(auction.values()))