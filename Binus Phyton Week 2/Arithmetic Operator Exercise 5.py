# Distance Between Two Points on Earth (Haversine Formula)
import math

#INPUT
lon1 = float(input("Enter longitude of point A: "))
lat1 = float(input("Enter latitude of point A: "))
lon2 = float(input("Enter longitude of point B: "))
lat2 = float(input("Enter latitude of Point B: "))

#PROCESS
R = 6371 #Earth's radius in km

#Convert degrees to radians
lat1 = math. radians(lat1)
lon2 = math. radians(lon1)
lat2 = math. radians(lat2)
lon2 = math. radians(lon2)

#Differences
dlat = lat2 - lat1
dlon = lon2 - lon1

#Haversine formula
a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
distance = R * c

#OUTPUT
print(f" The distance between the two points is {distance. 2f} km")