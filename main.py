import sys

places = {1 : "The North Pole", 2 : "Hollywood", 3 : "Swimming Pool"}

for num in places:
    print (places[num])

places[4] = "Washington DC"
print ("obj/" + places)
for num in places:
    print (places[num])