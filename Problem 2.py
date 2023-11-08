import math
radius1 = float(input('Enter Radius:'))
if radius1 > 0:
    area1 = math.pi * radius1 * radius1
    print(area1)
else:
    print('Invalid Inupt')