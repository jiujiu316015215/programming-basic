import math

radius_str = input( "Enter the radius of the circle: " )

radius_int = int( radius_str )

circunference = 2 * math.pi * radius_int
area = math.pi * pow(radius_int, 2)

print ( "Circunference is:",circunference,"area is:",area )
