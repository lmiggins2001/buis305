for count in range(0, 11, 1):
 print(count, end = " ")
for count in range(1, 11, 1):
 print(count, end = " ")
for count in range(1, 11, 2):
    print(count, end=" ")

import math
radius = float(input('Enter the radius'))
if radius> 0:
 radius = math.pi *radius*radius
 print('The radius is', radius)
else:
    print('Error: the area must be a positive number')

import math
radius = float(input('Enter the radius:'))
if(radius> 0):
 area = math.pi*radius*radius
 print('Area', area)
else:
     print('Error: the area must be a positive number')

lenght= float(input('Enter Lenght= '))
Breadth=float(input('Enter Breadth='))
area= lenght*Breadth
print(area)

Length= float(input('Enter Lenght= '))
Breadth=float(input('Enter Breadth='))
if(Length>0):
   print('valid input')
if(Breadth>0):
   print('Valid input')
   area= Length * Breadth
   print(area)
else:
   print('Invalid Input')
