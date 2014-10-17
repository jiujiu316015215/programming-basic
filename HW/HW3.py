print ("Welcome to May's Dungeon!")
currentroom = "c"
command = "c"
currentroom = "kitchen"

while (command != "q"):
	if currentroom == "kitchen":
		command = input ("You are in the kitchen. There are doors to the west(w),south(s) and east(e)")
		if command == "s":
			currentroom = "furnace"
		elif command == "w":
		    currentroom = "hallway"
		elif command == "e":
			currentroom = "livingroom"
	elif currentroom == "livingroom":
		command = input ("You are in the living room. There is door to the west(w)")
		if command == "w":
			currentroom = "kitchen"
	elif currentroom == "hallway":
		command = input ("You are in the hallway. There are doors to the south(s) and east(e)")
		if command == "s":
			currentroom = "library"
		elif command == "e":
			currentroom = "kitchen"
	elif currentroom == "library":
		print ("You are in the library. You found the Princess! You are a hero!")
		command = "q"
	elif currentroom == "furnace":
		print ("You enter the furnace and fry yourself to death!")
		command = "q"
		
print ("Goodbye!")


