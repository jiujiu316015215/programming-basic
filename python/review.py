#review

temperature = ''
temperature_int = int

while (temperature_int != 0):
	temperature = input("what's the temperature?")
	temperature_int = int (temperature)
	if temperature_int > 90:
		print ("it is hot")
	elif temperature_int < 50:
		print ("it is cold")
	elif temperature_int >= 51 and temperature_int <= 89:
		print ("it is just right")
