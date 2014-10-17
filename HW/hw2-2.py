import math

real_str = input ("Enter the real power:")
real_int = int (real_str)

reactive_str = input ("Enter the reactive power:")
reactive_int = int (reactive_str)

apparent = math.sqrt( pow(real_int,2) + pow(reactive_int,2))

factor = round(real_int / apparent,4)

print (" The power factor is:",format(factor,'.2%'))
