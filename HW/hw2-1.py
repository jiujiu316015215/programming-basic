import math

second = 365 * 24 * pow(60,2)

birth = second / 8

death = second / 13

immigrant = second / 40

popution = 318892103 + birth - death + immigrant

print ("The population will be",popution)

