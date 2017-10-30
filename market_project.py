#backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
#backpack.remove('xylophone')
#print "I will take " + str(len(backpack)) + " things away from you!"


#backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
#inventory = {}
#inventory['pocket']= 'seashell', 'strange berry', 'lint'
#inventory['backpack'] = backpack
#inventory['backpack'].sort()
#backpack.remove('dagger')
#backpack.append('gold')
#inventory['gold'] = 500
#print inventory
#inventory['gold'] = inventory['gold'] + 50
#print backpack
#backpack.remove('gold')
#print inventory

prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for key in prices:
  print "I want a(n) " + key
  print "It is " + str(prices[key]) + " dollars"
  print "The stock of the " + key + " is " + str(stock[key])
  #" which is " + str(prices[x]) + " and a stock of " + str(stock[x])

prices = {"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

for key in prices:
  print "I want a(n) " + key
  print "It is %s dollars" % prices[key]
  print "The stock of the " + key + " is %s" % stock[key]
